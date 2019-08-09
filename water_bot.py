import telebot
import time

access_token = '922889346:AAFUfryqEQgZ6Vk0z740exCrHDrLgULFdMg'
bot = telebot.TeleBot(access_token)
txt = '\n\nБот будет отправлять каждый час напоминание,\n что нужно попить!'


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет, ' + message.from_user.first_name +
                 ', для начала работы бота напиши команду /startdrinking.' + txt)


@bot.message_handler(commands=['startdrinking'])
def drinkwater(message):
    chat_id = message.chat.id
    for i in range(100000000):
        bot.send_message(
            chat_id, message.from_user.first_name + ', выпей стакан воды!')
        time.sleep(3600)


if __name__ == '__main__':
    bot.polling(none_stop=True)
