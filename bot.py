import telebot
from telebot import types

TOKEN = "8899376958:AAGHXKClNvMKaq2eON6WxoRhsU9Ut-VE0NI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🏡 Deluxe Village haqida")
    btn2 = types.KeyboardButton("🏠 Xonalar")
    btn3 = types.KeyboardButton("💰 Narxlar")
    btn4 = types.KeyboardButton("🍽️ Xizmatlar")
    btn5 = types.KeyboardButton("📍 Lokatsiya")
    btn6 = types.KeyboardButton("📅 Bron qilish")
    btn7 = types.KeyboardButton("☎️ Administrator")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn7)

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! Deluxe Village dam olish maskaniga xush kelibsiz.",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def menu(message):

    if message.text == "🏡 Deluxe Village haqida":
        bot.reply_to(message, "Deluxe Village — Oqtoshdagi zamonaviy dam olish maskani.")

    elif message.text == "🏠 Xonalar":
        bot.reply_to(message, "Xonalar rasmlari tez orada joylashtiriladi.")

    elif message.text == "💰 Narxlar":
        bot.reply_to(
            message,
            "Juma-Shanba: 450 000 so'm\nBoshqa kunlar: 350 000 so'm\n4 mahal ovqat kiritilgan."
        )

    elif message.text == "🍽️ Xizmatlar":
        bot.reply_to(
            message,
            "✅ 4 mahal ovqat\n✅ Basseyn\n✅ Sauna\n✅ Wi-Fi"
        )

    elif message.text == "📍 Lokatsiya":
        bot.reply_to(
            message,
            "https://yandex.ru/maps/?whatshere%5Bpoint%5D=69.758814,41.653309"
        )

    elif message.text == "📅 Bron qilish":
        bot.reply_to(message, "@Deluxe_village")

    elif message.text == "☎️ Administrator":
        bot.reply_to(message, "+998997833100")

print("Bot ishga tushdi...")
bot.infinity_polling()