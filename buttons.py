from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Кнопка для отправки номера телефона
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    number = KeyboardButton('Поделиться контактом', request_contact=True)

    kb.add(number)

    return kb

#Кнопка для отправки локации
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    location = KeyboardButton('Отправить локацию', request_location=True)

    kb.add(location)

    return kb

#Кнопка для выбора пола
def  gender_kb():
    kb = KeyboardButton(resize_keyboard=True)

    Male = KeyboardButton ('Муж👨‍')
    Female = KeyboardButton ('Жен👩')

    kb.add(Male,Female)

    return kb
#Кнопка для выбора количевства
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    buttons = [KeyboardButton(str(i)) for i in range(1, 10)]
    back = KeyboardButton('Назад')

    kb.add(*buttons, back)

    return kb

#Кнопки для корзины
def  backet_kb():
    kb = KeyboardButton(resize_keyboard=True)

    button1 = KeyboardButton('Очистить‍')
    button2 = KeyboardButton('Оформить')
    button3 = KeyboardButton('Редактировать')
    button4 = KeyboardButton('Назад')

    kb.add(button1, button2, button3, button4)

    return kb

#Кнопки при выборе способа оплаты
def pay_type_kb():
    kb = KeyboardButton(resize_keyboard=True)

    button1 = KeyboardButton('Наличные‍')
    button2 = KeyboardButton('Картой')
    button3 = KeyboardButton('Назад')

    kb.add(button1, button2, button3)

    return kb

#Кнопки для подтверждения заказа
def confirm_kb():
    kb = KeyboardButton(resize_keyboard=True)

    button1 = KeyboardButton('Подтвердить‍')
    button2 = KeyboardButton('Отменить')
    button3 = KeyboardButton('Назад')

    kb.add(button1, button2, button3)

    return kb


#Кнопки с названиями товаров
def products_kb():
    pass