import telebot
from telebot import types
bot = telebot.TeleBot('5882346362:AAFZiqb-8HKhwPMpMyehS_dEjDSHU-jRiFE')
@bot.message_handler(content_types=['text', 'photo'])

def get_text_messages(message):
    if message.text == "Привет!" or message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, это КОТОБОТ!")
    elif message.text.strip() == "Серый":
        bot.send_photo(message.from_user.id, 'https://koshka.top/uploads/posts/2021-12/1639021684_4-koshka-top-p-milii-serii-kotenok-4.jpg')
    elif message.text.strip() == "Рыжий":
        bot.send_photo(message.from_user.id, 'https://img.freepik.com/premium-photo/a-beautiful-bright-red-kitten-on-a-white-background-looks-to-the-side-young-cute-little-red-kitty-long-haired-ginger-kitten-play-at-home-cute-funny-home-pets-space-for-text_332694-193.jpg')
    elif message.text.strip() == "Чёрный":
        bot.send_photo(message.from_user.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPGRYcmuolsIF_h2is9sbRJ-ZDrixrs-AKg&usqp=CAU')
    elif message.text.strip() == "С пятнышком":
        bot.send_photo(message.from_user.id, 'https://wonder-day.com/wp-content/uploads/2022/06/wonder-day-very-cute-kitty-pictures-26.jpg')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Выбери, какого котика хочешь посмотреть. У нас есть серый, рыжий, чёрный и с пятнышком")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help или Привет!.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Серый")
    item2 = types.KeyboardButton("Рыжий")
    item3 = types.KeyboardButton("Чёрный")
    item5 = types.KeyboardButton("С пятнышком")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item5)
    question = 'Тебе какого котика?'
    bot.send_message(message.from_user.id, text=question, reply_markup=markup)


bot.polling(none_stop=True, interval=0)