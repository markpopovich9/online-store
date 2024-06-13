import telebot

inline_button1=telebot.types.InlineKeyboardButton(text= "inline_button1", callback_data="1")
inline_button2=telebot.types.InlineKeyboardButton(text= "inline_button2", callback_data="2")
inline_keyboard=telebot.types.InlineKeyboardMarkup([[inline_button2, inline_button1]])
bot = telebot.TeleBot('6669027800:AAH0Cj4rJmqArmz5RAsVd0fMfS9uX-XrIFA')
list_moderators = [{"id": 2036291862, "name": "Illya"}]

@bot.message_handler(["start"])
def start(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="Bomjour", reply_markup= inline_keyboard)
# @bot.register_next_step_handler()
# def next(message: telebot.types.Message):
#     bot.send_message(chat_id=message.chat.id, text="Hello")
@bot.callback_query_handler(lambda call: True if call.data == "1" else False)
def callbacks(callback: telebot.types.CallbackQuery):
    id  = callback.message.chat.id
    is_moderator = False
    for moderator in list_moderators:
        if moderator["id"]== id:
            is_moderator = True
            break  
    if is_moderator:

        bot.send_message(chat_id=id , text="Hello" )
    else:
        bot.send_message(chat_id=id , text="Hello's" )
    print(callback.message.chat.id)

@bot.callback_query_handler(lambda call: True if call.data == "2" else False)
def callbacks(callback: telebot.types.CallbackQuery):
   bot.send_message(chat_id=callback.message.chat.id, text="Hi" )

   
bot.polling()