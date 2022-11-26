import telebot
import _token
import functions

bot = telebot.TeleBot(_token.API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    functions.start_message(message)


@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.chat.id, f'{message.text}')


bot.polling()
