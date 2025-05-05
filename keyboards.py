from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import BANKS


def get_document_type_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Квитанция", callback_data="type:receipt"),
            InlineKeyboardButton(text="Чек", callback_data="type:check")
        ],
        [InlineKeyboardButton(text="Отмена", callback_data="cancel")]
    ])
    return keyboard


def get_bank_keyboard(doc_type: str) -> InlineKeyboardMarkup:
    banks_dict = BANKS["receipts"] if doc_type == "receipt" else BANKS["checks"]

    buttons = []
    row = []
    for bank_code, bank_info in banks_dict.items():
        if len(row) == 2:
            buttons.append(row)
            row = []

        row.append(InlineKeyboardButton(
            text=bank_info["name"],
            callback_data=f"bank:{doc_type}:{bank_code}"
        ))

    if row:
        buttons.append(row)

    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back:type")])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_confirmation_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="confirm"),
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ])
    return keyboard


def get_restart_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Создать новый документ", callback_data="restart")]
    ])
    return keyboard
