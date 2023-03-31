
import telebot
bot = telebot.TeleBot("6247235842:AAHuYfAC5WYD5fFSZ2uifPvwIL-JNWQhzv0")
@bot.message_handler(command=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет я умею /register")
    bot.register_next_step_handler(message)

