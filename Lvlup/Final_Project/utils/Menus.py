def buttons_1(message, bot): # первая менюха
    from telebot import types
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Наши адреса')
    btn2 = types.KeyboardButton('Наш Сайт')
    btn3 = types.KeyboardButton('Рассказать о Растениях')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Задайте интересующий вас вопрос или выберите кнопку внизу😋', reply_markup=markup)

def buttons_2(message, bot): # вторая менюха
    from telebot import types
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Петунии')
    btn2 = types.KeyboardButton('Розы')
    btn3 = types.KeyboardButton('Туи')
    btn4 = types.KeyboardButton('Вернуться в главное меню')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Задайте интересующий вас вопрос или выберите кнопку внизу😋', reply_markup=markup)

def opne_file(file_name):
    with open(f'../Final_Project/Files/{file_name}', mode='r', encoding='utf8') as f:
        file_read = f.read()
        return file_read