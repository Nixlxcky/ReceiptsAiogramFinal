from aiogram import Router, F, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile, InputMediaPhoto

from keyboards import (
    get_document_type_keyboard,
    get_bank_keyboard,
    get_confirmation_keyboard,
    get_restart_keyboard

)
from config import BANKS, FIELD_NAMES
from utils.helper import generate_document, clean_old_files

router = Router()


class GenerationStates(StatesGroup):
    waiting_for_type = State()
    waiting_for_bank = State()
    waiting_for_field = State()
    waiting_for_confirmation = State()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    clean_old_files()

    photo = FSInputFile("welcome.png")
    await message.answer_photo(
        photo=photo,
        caption="Добро пожаловать в генератор чеков и квитанций!\n"
                "Выберите тип документа, который хотите создать:",
        reply_markup=get_document_type_keyboard()
    )

    await state.set_state(GenerationStates.waiting_for_type)

    await state.update_data(message_id=message.message_id + 1)


@router.callback_query(F.data == "restart")
async def process_restart(callback: CallbackQuery, state: FSMContext):
    clean_old_files()

    photo = FSInputFile("welcome.png")

    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=photo,
            caption="Выберите тип документа, который хотите создать:",
        ),
        reply_markup=get_document_type_keyboard()
    )
    await state.clear()
    await state.set_state(GenerationStates.waiting_for_type)
    await state.update_data(message_id=callback.message.message_id)


@router.callback_query(F.data == "cancel")
async def process_cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_caption(
        caption="Операция отменена. Нажмите кнопку, чтобы начать снова.",
        reply_markup=get_restart_keyboard()
    )
    await callback.answer("Операция отменена")
    await state.clear()


@router.callback_query(F.data == "back:type")
async def process_back_to_type(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_caption(
        caption="Выберите тип документа, который хотите создать:",
        reply_markup=get_document_type_keyboard()
    )
    await state.set_state(GenerationStates.waiting_for_type)
    await callback.answer()


@router.callback_query(F.data.startswith("type:"))
async def process_type_selection(callback: CallbackQuery, state: FSMContext):
    doc_type = callback.data.split(":")[1]

    await state.update_data(doc_type=doc_type)

    await callback.message.edit_caption(
        caption=f"Вы выбрали: {'Квитанцию' if doc_type == 'receipt' else 'Чек'}\n"
                f"Теперь выберите банк:",
        reply_markup=get_bank_keyboard(doc_type)
    )

    await state.set_state(GenerationStates.waiting_for_bank)
    await callback.answer()


@router.callback_query(F.data.startswith("bank:"))
async def process_bank_selection(callback: CallbackQuery, state: FSMContext):
    _, doc_type, bank_code = callback.data.split(":")

    await state.update_data(bank_code=bank_code)

    bank_type = "receipts" if doc_type == "receipt" else "checks"
    fields = BANKS[bank_type][bank_code]["fields"]


    await state.update_data(user_data={})

    await state.update_data(fields=fields, current_field_index=0)


    await request_next_field(callback.message, state)

    await state.set_state(GenerationStates.waiting_for_field)
    await callback.answer()


async def request_next_field(message, state: FSMContext):
    data = await state.get_data()
    fields = data.get("fields", [])
    current_index = data.get("current_field_index", 0)

    if current_index < len(fields):
        field = fields[current_index]
        field_name = FIELD_NAMES.get(field, field)

        await message.edit_caption(
            caption=f"Введите {field_name}:"
        )
    else:
        user_data = data.get("user_data", {})
        doc_type = data.get("doc_type")
        bank_code = data.get("bank_code")
        bank_type = "receipts" if doc_type == "receipt" else "checks"

        confirmation_text = f"Данные для {'квитанции' if doc_type == 'receipt' else 'чека'} {BANKS[bank_type][bank_code]['name']}:\n\n"

        for field, value in user_data.items():
            if field not in ["template_path", "output_path"]:
                field_name = FIELD_NAMES.get(field, field)
                confirmation_text += f"{field_name}: {value}\n"

        confirmation_text += "\nПодтвердите генерацию документа:"

        await message.edit_caption(
            caption=confirmation_text,
            reply_markup=get_confirmation_keyboard()
        )

        await state.set_state(GenerationStates.waiting_for_confirmation)


@router.message(GenerationStates.waiting_for_field)
async def process_field_input(message: Message, state: FSMContext):
    data = await state.get_data()
    message_id = data.get("message_id")
    fields = data.get("fields", [])
    current_index = data.get("current_field_index", 0)
    user_data = data.get("user_data", {})

    current_field = fields[current_index]
    user_data[current_field] = message.text

    await state.update_data(
        user_data=user_data,
        current_field_index=current_index + 1
    )

    try:
        await message.delete()
        await message.bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=message_id,
            caption="Обработка..."
        )

        await request_next_field(await message.bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=message_id
        ), state)
    except Exception:
        await message.delete()


@router.callback_query(GenerationStates.waiting_for_confirmation, F.data == "confirm")
async def process_confirmation(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    doc_type = data.get("doc_type")
    bank_code = data.get("bank_code")
    user_data = data.get("user_data", {})

    await callback.message.edit_caption(caption="Генерация документа...")

    try:

        output_path = generate_document(doc_type, bank_code, user_data)

        document = FSInputFile(output_path)

        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=document,
                caption=f"Документ успешно сгенерирован!\nНажмите на кнопку, чтобы создать новый документ."
            ),
            reply_markup=get_restart_keyboard()
        )

    except Exception as e:
        await callback.message.edit_caption(
            caption=f"Произошла ошибка при генерации документа: {str(e)}\n"
                    f"Нажмите на кнопку, чтобы начать заново.",
            reply_markup=get_restart_keyboard()
        )

    await state.clear()
    await callback.answer()


def register_handlers(dp: Dispatcher):
    dp.include_router(router)
