import telebot

TOKEN = "7638667821:AAE_wzlfq21NsTN-dIXd-Wa7HNNWi_82GWM"
ADMIN_ID = 1877319408  # Sizning Telegram ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "🍔 Yummy Food buyurtma botiga xush kelibsiz!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "✅ Buyurtmangiz qabul qilindi!")

bot.infinity_polling()
