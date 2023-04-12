import telebot
from telebot import types
from Final_Project.utils.Menus import buttons_1, buttons_2, opne_file
import config
bot = telebot.TeleBot(config.bot_adress)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user))
    bot.send_message(message.chat.id, "Я помогу вам в ваших вопросах, я могу рассказать вам о различных растениях, способах ухода за ними и прочие интересные штуки")
    bot.send_message(message.chat.id, "На нашем сайте вы можете сделать заказ и ознакомиться с различными услугами")
    buttons_1(message,bot)

@bot.message_handler(content_types=['text'])
def read_text(message):
    if message.text == "Наши адреса":
        with open('../Final_Project/Files/Adress.txt', mode='r', encoding='utf8') as f:
             file_read = f.read()
        bot.send_message(message.chat.id, f"Найти нас вы сможете по адресу: {file_read}")
    elif message.text == 'Сайт' or message.text == 'Наш Сайт' or message.text == 'cайт':
        bot.send_message(message.chat.id, "Наш адрес в интернете: https://pitomnik-bugrovka.ru/services")
    elif message.text == "Рассказать о Растениях":
        buttons_2(message, bot)
    elif message.text == "Вернуться в главное меню":
        bot.send_message(message.chat.id, "Вы вернулись в главное меню")
        buttons_1(message,bot)
    elif message.text == "Петунии" or message.text == "Петуния":
        message.text = 'Петунии'+'.txt'
        bot.send_message(message.chat.id, f"{opne_file(message.text)}")
    elif message.text == "Розы" or message.text == "Роза":
        message.text = 'Розы'+'.txt'
        bot.send_message(message.chat.id, f"{opne_file(message.text)}")
    elif message.text == "Туи" or message.text == "Туя":
        message.text = 'Туи'+'.txt'
        bot.send_message(message.chat.id, f"{opne_file(message.text)}")
    else:
        bot.send_message(message.chat.id, "Этого я пока не знаю, но скоро обязательно научусь, а пока спроси что-то другое.")

#bot.infinity_polling()
bot.polling(none_stop=True, interval=0)