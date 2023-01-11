# project, telegram bot in облаке

import telebot
#import ftoken

#bot = telebot.TeleBot(ftoken.TOKEN)
bot = telebot.TeleBot('5854220388:AAHlsY1xpcoHbyijDyIILqj2yYblVzxaDvw')

@bot.message_handler(content_types=['text'])
def xat(message):
    bot.send_message(message.chat.id, message.text)

#RUN ЗАПУСК
bot.polling(none_stop=True)

