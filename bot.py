import telebot
import random
import test

bot = telebot.TeleBot('1126937460:AAGAZNrmaJo8A2AzTgT6WBJwcZ5jTa9r0ig')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Твоє побажання на сьогодні')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, Давай знайомитись, я Бот який передбачає майбутнє', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'твоє побажання на сьогодні':
		bot.send_message(message.chat.id, random.choice(test.quot) )
		

			

bot.polling()


