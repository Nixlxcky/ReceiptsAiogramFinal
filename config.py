import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

BANKS = {
    "receipts": {
        "TBANK": {
            "name": "Т-Банк",
            "fields": ["date", "total", "sender", "phone_number", "receiver"]
        },
        "ALFA": {
            "name": "Альфа Банк",
            "fields": ["creation_date", "send_date", "total", "receiver", "receiver_bank", "phone_number", "identifier"]
        },
        "RAJF": {
            "name": "Райффайзен Банк",
            "fields": ["date", "time", "payer", "total", "receiver", "phone_number", "receiver_bank"]
        },
        "GASPROMBANK": {
            "name": "Газпромбанк",
            "fields": ["date_and_time", "phone_number", "receiver", "receiver_bank", "sender", "sum", "commission",
                       "total", "operation_number"]
        },
        "SBER": {
            "name": "Сбербанк",
            "fields": ["date", "receiver", "phone_number", "receiver_bank", "sender", "total", "identifier"]
        },
        "VTB": {
            "name": "ВТБ",
            "fields": ["receiver", "date", "payer", "phone_number", "receiver_bank", "identifier", "total"]
        }
    },

    "checks": {
        "MTS": {
            "name": "МТС Банк",
            "fields": ["time", "amount", "transaction_date", "card_info", "account_number", "transaction_code"],
            "template": "Samples/MTS_check.jpeg"
        },
        "SBER": {
            "name": "Сбербанк",
            "fields": ["time", "amount", "sender_bank"],
            "template": "Samples/SBER_check.jpg"
        },
        "ALFA": {
            "name": "Альфа Банк",
            "fields": ["time", "amount", "transaction_date", "receiver_account", "payment_details"],
            "template": "Samples/ALFA_check.jpeg"
        },
        "TBANK": {
            "name": "Т-Банк",
            "fields": ["time", "transaction_date", "amount"],
            "template": "Samples/TBANK_check.jpeg"
        }
    }
}

FIELD_NAMES = {
    "date": "Дата (например, 08.01.2025 22:43:57)",
    "total": "Сумма (например, 69 322 ₽)",
    "sender": "Отправитель (ФИО)",
    "phone_number": "Номер телефона (например, +7 (951) 806-62-56)",
    "receiver": "Получатель (ФИО)",
    "creation_date": "Дата создания (например, 08.01.2025 14:08 мск)",
    "send_date": "Дата отправки (например, 08.01.2025 14:04:50 мск)",
    "receiver_bank": "Банк получателя (например, Сбербанк)",
    "identifier": "Идентификатор перевода (например, A5008110451038040000080011410901)",
    "time": "Время (например, 10:04)",
    "payer": "Плательщик (ФИО)",
    "date_and_time": "Дата и время (например, 21.12.2024 в 15:00 (МСК))",
    "sum": "Сумма перевода (например, 50 234,00 руб.)",
    "commission": "Комиссия (например, 60,50 руб.)",
    "operation_number": "Номер операции (например, А435611595793900000006IA00000051)",
    "amount": "Сумма (например, 24 881 RUB)",
    "transaction_date": "Дата транзакции (например, 31 января 2024 · 16:03)",
    "card_info": "Информация о карте (например, Кредитная CASHBACK •• 4231)",
    "account_number": "Номер счета (например, 40817 81090 30078 72312)",
    "transaction_code": "Код транзакции (например, 505121961616)",
    "sender_bank": "Банк отправителя (например, Перевод из Альфа Банк)",
    "receiver_account": "Счет получателя (например, Счёт кредитной карты ··1839)",
    "payment_details": "Детали платежа (например, Внутрибанковский перевод между счетами, ТУМАНОВ А. К.)",
    "template_path": "Путь к шаблону",
    "output_path": "Путь сохранения"
}