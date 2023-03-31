import telebot
from Homework.Homework_3.Homework3_1v2 import calculator

bot = telebot.TeleBot("6247235842:AAHuYfAC5WYD5fFSZ2uifPvwIL-JNWQhzv0")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я спер пупер бот и я умею вычислять простые примеры, что бы воспользоваться калькулятором введите /calc")
@bot.message_handler(commands=['calc'])
def calc(message):
    bot.send_message(message.chat.id, "Введите пожалуйста пример")
    bot.register_next_step_handler(message, read_operation)
def read_operation(message):
    operation = message.text
    bot.send_message(message.chat.id, f"Ответ:{operation} = {calculator(operation)}")

bot.infinity_polling()