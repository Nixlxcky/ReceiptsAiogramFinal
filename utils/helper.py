import os

from utils.drawer import (
    generateTBANKReceipt, generateALFAReceipt, generateRAJFReceipt,
    generateGASPROMBANKReceipt, generateSBERReceipt, generateVTBReceipt,
    generateMTSCheck, generateSBERCheck, generateALFACheck, generateTBANKCheck
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")


def generate_document(doc_type, bank_code, user_data):
    output_path = ""

    if doc_type == "receipt":
        if bank_code == "TBANK":
            output_path = generateTBANKReceipt(**user_data)
        elif bank_code == "ALFA":
            output_path = generateALFAReceipt(**user_data)
        elif bank_code == "RAJF":
            output_path = generateRAJFReceipt(**user_data)
        elif bank_code == "GASPROMBANK":
            output_path = generateGASPROMBANKReceipt(**user_data)
        elif bank_code == "SBER":
            output_path = generateSBERReceipt(**user_data)
        elif bank_code == "VTB":
            output_path = generateVTBReceipt(**user_data)


    elif doc_type == "check":
        if bank_code == "MTS":
            output_path = generateMTSCheck(**user_data)
        elif bank_code == "SBER":
            output_path = generateSBERCheck(**user_data)
        elif bank_code == "ALFA":

            output_path = generateALFACheck(**user_data)
        elif bank_code == "TBANK":

            output_path = generateTBANKCheck(**user_data)

    return output_path


def clean_old_files():
    for filename in os.listdir(TEMP_DIR):
        file_path = os.path.join(TEMP_DIR, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
