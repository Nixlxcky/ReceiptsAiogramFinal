import os

from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")


def get_path(base, filepath):
    return os.path.join(base, filepath)


def generateTBANKReceipt(

        date: str,
        total: str,
        sender: str,
        phone_number: str,
        receiver: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/TBANK_receipt.png'))
    sample_draw = ImageDraw.Draw(sample)

    font_small = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/TinkoffSans/TinkoffSans-Regular.ttf'), 38)
    font_base = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/TinkoffSans/TinkoffSans-Regular.ttf'), 40)
    font_big = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/TinkoffSans/TinkoffSans-Medium.ttf'), 56)

    sample_draw.text((440, 807), date, font=font_small, fill=(115, 115, 115), anchor='rb')

    sample_draw.text((1184, 901), total, font=font_big, fill=(30, 30, 30), anchor='rb')

    sample_draw.text((1184, 1252), total, font=font_base, fill=(55, 55, 55), anchor='rb')
    sample_draw.text((1184, 1438), sender, font=font_base, fill=(55, 55, 55), anchor='rb')
    sample_draw.text((1184, 1531), phone_number, font=font_base, fill=(55, 55, 55), anchor='rb')
    sample_draw.text((1184, 1624), receiver, font=font_base, fill=(55, 55, 55), anchor='rb')

    path = get_path(TEMP_DIR, "TBANK_receipt_generated.png")
    sample.save(path)
    return path


def generateALFAReceipt(
        creation_date: str,
        send_date: str,
        total: str,
        receiver: str,
        receiver_bank,
        phone_number: str,
        identifier: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/ALFA_receipt.png'))
    sample_draw = ImageDraw.Draw(sample)

    font_base = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/San Francisco Pro Text/SFProText-Medium.ttf'), 24)

    sample_draw.text((1210, 688), creation_date, font=font_base, fill=(115, 115, 115), anchor='rb')

    sample_draw.text((85, 953), total, font=font_base, fill='black')
    sample_draw.text((660, 953), phone_number, font=font_base, fill='black')
    sample_draw.text((660, 1055), receiver_bank, font=font_base, fill='black')
    sample_draw.text((85, 1156), send_date, font=font_base, fill='black')
    sample_draw.text((660, 1258), identifier, font=font_base, fill='black')
    sample_draw.text((85, 1359), receiver, font=font_base, fill='black')

    path = get_path(TEMP_DIR, "ALFA_receipt_generated.png")
    sample.save(path)
    return path


def generateRAJFReceipt(
        date: str,
        time: str,
        payer: str,
        total,
        receiver: str,
        phone_number,
        receiver_bank: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/RAJF_receipt.png'))
    sample_draw = ImageDraw.Draw(sample)

    font_base = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/arial/ARIAL.TTF'), 20)

    sample_draw.text((181, 360), date, font=font_base, fill=(55, 55, 55))
    sample_draw.text((492, 360), time, font=font_base, fill=(55, 55, 55))

    sample_draw.text((371, 642), payer, font=font_base, fill=(55, 55, 55))
    sample_draw.text((371, 741), total, font=font_base, fill=(55, 55, 55))
    sample_draw.text((371, 877), receiver, font=font_base, fill=(55, 55, 55))
    sample_draw.text((371, 928), phone_number, font=font_base, fill=(55, 55, 55))
    sample_draw.text((371, 977), receiver_bank, font=font_base, fill=(55, 55, 55))

    path = get_path(TEMP_DIR, "RAJF_receipt_generated.jpg")
    sample.save(path)
    return path


def generateGASPROMBANKReceipt(
        date_and_time: str,
        phone_number: str,
        receiver: str,
        receiver_bank: str,
        sender: str,
        sum: str,
        commission: str,
        total: str,
        operation_number: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/GASPROMBANK_receipt.png'))
    sample_draw = ImageDraw.Draw(sample)

    font_base = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/Proxima Nova/proximanovacond_bold.ttf'), 45)

    sample_draw.text((81, 785), date_and_time, font=font_base, fill='black')
    sample_draw.text((81, 1317), phone_number, font=font_base, fill='black')
    sample_draw.text((81, 1450), receiver, font=font_base, fill='black')
    sample_draw.text((81, 1583), receiver_bank, font=font_base, fill='black')
    sample_draw.text((81, 1716), sender, font=font_base, fill='black')
    sample_draw.text((81, 1849), sum, font=font_base, fill='black')
    sample_draw.text((81, 1982), commission, font=font_base, fill='black')
    sample_draw.text((81, 2115), total, font=font_base, fill='black')
    sample_draw.text((81, 2248), operation_number, font=font_base, fill='black')

    path = get_path(TEMP_DIR, "GASPROMBANK_receipt_generated.png")
    sample.save(path)
    return path


def generateSBERReceipt(
        date: str,
        receiver: str,
        phone_number: str,
        receiver_bank: str,
        sender: str,
        total: str,
        identifier: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/SBER_receipt.png'))
    sample_draw = ImageDraw.Draw(sample)

    font_base = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/arial/ARIAL.TTF'), 46)

    sample_draw.text((297, 694), date, font=font_base, fill=(115, 115, 115))

    sample_draw.text((107, 1143), receiver, font=font_base, fill='black')
    sample_draw.text((107, 1306), phone_number, font=font_base, fill='black')
    sample_draw.text((107, 1478), receiver_bank, font=font_base, fill='black')
    sample_draw.text((107, 1683), sender, font=font_base, fill='black')
    sample_draw.text((107, 2060), total, font=font_base, fill='black')
    sample_draw.text((107, 2399), identifier, font=font_base, fill='black')

    path = get_path(TEMP_DIR, "SBER_receipt_generated.png")
    sample.save(path)
    return path


def generateVTBReceipt(
        receiver: str,
        date: str,
        payer: str,
        phone_number: str,
        receiver_bank: str,
        identifier: str,
        total: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/VTB_receipt.png'))
    sample_draw = ImageDraw.Draw(sample)

    font_base = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/San Francisco Pro Text/SFProText-Regular.ttf'), 38)
    font_medium = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/San Francisco Pro Text/SFProText-Regular.ttf'), 44)
    font_big = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/San Francisco Pro Text/SFProText-Regular.ttf'), 56)

    sample_draw.text((872, 872), receiver, font=font_medium, fill=(40, 40, 40), anchor='rb')

    sample_draw.text((1159, 1114), date, font=font_base, fill=(40, 40, 40), anchor='rb')
    sample_draw.text((1159, 1327), payer, font=font_base, fill=(40, 40, 40), anchor='rb')
    sample_draw.text((1159, 1433), receiver, font=font_base, fill=(40, 40, 40), anchor='rb')
    sample_draw.text((1159, 1540), phone_number, font=font_base, fill=(40, 40, 40), anchor='rb')
    sample_draw.text((1159, 1647), receiver_bank, font=font_base, fill=(40, 40, 40), anchor='rb')

    if len(identifier) > 26:
        sample_draw.text((1159, 1747), identifier[:25], font=font_base, fill=(40, 40, 40), anchor='rb')
        sample_draw.text((1159, 1800), identifier[25:], font=font_base, fill=(40, 40, 40), anchor='rb')
    else:
        sample_draw.text((1159, 1747), identifier, font=font_base, fill=(40, 40, 40), anchor='rb')

    sample_draw.text((1159, 2014), total, font=font_base, fill=(40, 40, 40), anchor='rb')

    sample_draw.text((1159, 2283), total, font=font_big, fill=(40, 40, 40), anchor='rb')

    path = get_path(TEMP_DIR , "VTB_receipt_generated.png")
    sample.save(path)
    return path


def generateMTSCheck(
        time: str,
        amount: str,
        transaction_date: str,
        card_info: str,
        account_number: str,
        transaction_code: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/MTS_check.jpeg'))
    sample_draw = ImageDraw.Draw(sample)

    iOS_font = ImageFont.truetype(get_path(BASE_DIR, "Fonts/San Francisco Pro Text/SF-Pro-Text-Semibold.otf"), 22)
    font_small = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/MTSSans/MTSSans-Regular.ttf'), 22)
    font_medium = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/MTSSans/MTSSans-Regular.ttf'), 26)
    font_large = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/MTSSans/MTSSans-Medium.ttf'), 32)

    green_color = (28, 176, 63, 255)
    text_color = (0, 0, 0)
    gray_color = (108, 108, 108, 128)

    sample_draw.text((125, 53), time, fill=text_color, font=iOS_font, anchor='rb')

    text_x = sample.width // 2
    sample_draw.text((text_x, 407), amount, fill=green_color, font=font_large, anchor='ms')
    sample_draw.text((text_x, 485), transaction_date, fill=gray_color, font=font_small, anchor='ms')

    sample_draw.text((31, 830), card_info, fill=text_color, font=font_medium)

    sample_draw.text((31, 895), "Счет зачисления", fill=gray_color, font=font_small)
    sample_draw.text((31, 932), account_number, fill=text_color, font=font_medium)

    sample_draw.text((31, 997), "Код транзакции", fill=gray_color, font=font_small)
    sample_draw.text((31, 1035), transaction_code, fill=text_color, font=font_medium)

    path = get_path(TEMP_DIR, 'MTS_check_generated')
    sample.save(path)
    return path


def generateSBERCheck(
        time: str,
        amount: str,
        sender_bank: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/SBER_check.jpg'))
    sample_draw = ImageDraw.Draw(sample)

    iOS_font = ImageFont.truetype(get_path(BASE_DIR, "Fonts/San Francisco Pro Text/SF-Pro-Text-Semibold.otf"), 22)
    font_small = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/sb-sans-text-medium.ttf'), 18)
    font_large = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/sb-sans-text-medium.ttf'), 42)

    white_color = (255, 255, 255)

    sample_draw.text((125, 53), time, fill=white_color, font=iOS_font, anchor='rb')

    text_x = sample.width // 2
    sample_draw.text((text_x, 391), amount, fill=white_color, font=font_large, anchor='ms')
    sample_draw.text((text_x, 444), sender_bank, fill=white_color, font=font_small, anchor='ms')

    path = get_path(TEMP_DIR, 'SBER_check_generated.png')
    sample.save(path)
    return path


def generateALFACheck(
        time: str,
        amount: str,
        transaction_date: str,
        receiver_account: str,
        payment_details: str
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/ALFA_check.jpeg'))
    sample_draw = ImageDraw.Draw(sample)

    iOS_font = ImageFont.truetype(get_path(BASE_DIR, "Fonts/San Francisco Pro Text/SF-Pro-Text-Semibold.otf"), 22)
    font_small = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/inter/Inter-Regular.otf'), 16)
    font_medium = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/inter/Inter-Regular.otf'), 20)
    font_large = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/inter/Inter-SemiBold.otf'), 32)

    green_color = (0, 173, 93)
    white_color = (255, 255, 255)
    gray_color = (155, 155, 155, 255)

    sample_draw.text((131, 49), time, fill=white_color, font=iOS_font, anchor='rb')
    sample_draw.text((29, 271), amount, fill=green_color, font=font_large)
    sample_draw.text((28, 364), transaction_date, fill=gray_color, font=font_small)
    sample_draw.text((28, 748), receiver_account, fill=white_color, font=font_medium)

    if len(payment_details) > 40:
        sample_draw.text((28, 845), payment_details[:40], font=font_medium, fill=white_color, )
        sample_draw.text((28, 879), payment_details[40:], font=font_medium, fill=white_color, )
    else:
        sample_draw.text((28, 845), payment_details, font=font_medium, fill=white_color, )

    path = get_path(TEMP_DIR, 'ALFA_check_generated.png')
    sample.save(path)
    return path


def generateTBANKCheck(
        time: str,
        transaction_date: str,
        amount: str,
):
    sample = Image.open(get_path(BASE_DIR, 'Samples/TBANK_check.jpeg'))
    sample_draw = ImageDraw.Draw(sample)

    iOS_font = ImageFont.truetype(get_path(BASE_DIR, "Fonts/San Francisco Pro Text/SF-Pro-Text-Semibold.otf"), 22)
    font_small = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/San Francisco Pro Text/SF-Pro-Text-Regular.otf'), 18)
    font_large = ImageFont.truetype(get_path(BASE_DIR, 'Fonts/San Francisco Pro Text/SF-Pro-Rounded-Bold.otf'), 42)

    green_color = (16, 190, 83, 235)
    white_color = (255, 255, 255)

    sample_draw.text((131, 49), time, fill=white_color, font=iOS_font, anchor='rb')

    text_x = sample.width // 2
    sample_draw.text((text_x, 151), transaction_date, fill=white_color, font=font_small, anchor='ms')
    sample_draw.text((text_x, 436), amount, fill=green_color, font=font_large, anchor='ms')

    path = get_path(TEMP_DIR, 'TBANK_check_generated.jpg')
    sample.save(path)
    return path


if __name__ == '__main__':
    pass

    """
    generateTBANKReceipt('08.01.2025  22:43:57', '69 322 ₽', 'Елена сергеевна', '+7 (951) 806-62-56', 'Александр Ф.')

    generateALFAReceipt('08.01.2025 14:08 мск', '08.01.2025 14:04:50 мск', '24 881 RUR', 'Егор Алексеевич К',
                        'Сбербанк', '79858769842', 'A5008110451038040000080011410901')

    generateRAJFReceipt('10.11.2024', '10.04.07', 'Румянцева Ирина Петровна', '4855.00 ₽', 'Иван Дмитриевич X',
                        '79191865214', 'Сбербанк')

    generateGASPROMBANKReceipt('21.12.2024 в 15:00 (МСК)', '+7(903)390-25-42', 'Диана Артемовна А.', 'Альфа Банк',
                               'Алексей Евгеньевич К.', '50 234,00 руб.', '60,50 руб.', '50 294,50 руб.',
                               'А435611595793900000006IA00000051')

    generateVTBReceipt('Максим Артемович Н.', '02.01.2025, 20:36', 'Анна Викторовна Т.', '+7(910) 597-42-68',
                       'Альфа Банк', 'B5002173555134030000110011410901', '74 687 ₽')

    generateSBERReceipt('23 января 2025 19:49:51 (МСК)', 'Рафаэль Артурович Ц', '+7 903 814-35-13', 'Т-Банк',
                        'Ирина Анатольевна Д.', '6500.00 ₽', 'B50231648194100K0000160011420701')
    """
