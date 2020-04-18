from telebot import TeleBot

token = ""

bot = TeleBot(token=token)


@bot.message_handler(commands=['start'])
def handle_start(message):
   return bot.send_message(chat_id=message.chat.id, text='Start komandasi tutildi')


if __name__ == "__main__":
    bot.polling()
