import string

from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from credits import bot_token
from googletrans import Translator

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

text = []

translator = Translator()


def start(update):
    reply_keyboard = [['en-> ru or ru -> en', 'de -> ru or ru->de', 'es-> ru or ru ->es']]
    update.message.reply_text('Добрый день! Отправьте, что надо перевести. Затем, выберите язык для перевода',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))


def number(update):
    global text
    text.append(str(update.message.text))


def translate_def(update, context):
    global text
    end_text = translator.translate(text[0]).text
    context.bot.send_message(update.effective_chat.id, end_text)
    text = []


def translate_ru(update, context):
    global text
    if text[0][0].upper() not in string.ascii_uppercase:
        end_text = translator.translate(text[0]).text
        context.bot.send_message(update.effective_chat.id, end_text)
    else:
        end_text = translator.translate(text[0], dest='ru').text
        context.bot.send_message(update.effective_chat.id, end_text)
    text = []


def translate_de(update, context):
    global text
    if text[0][0].upper() not in string.ascii_uppercase:
        end_text = translator.translate(text[0], dest="de").text
        context.bot.send_message(update.effective_chat.id, end_text)
    else:
        end_text = translator.translate(text[0], dest='ru').text
        context.bot.send_message(update.effective_chat.id, end_text)
    text = []


def translate_es(update, context):
    global text
    if text[0][0].upper() not in string.ascii_uppercase:
        end_text = translator.translate(text[0], dest="es").text
        context.bot.send_message(update.effective_chat.id, end_text)
    else:
        end_text = translator.translate(text[0], dest='ru').text
        context.bot.send_message(update.effective_chat.id, end_text)
    text = []


start_handler = CommandHandler('start', start)
multiplication_handler = MessageHandler(Filters.regex('^(en-> ru or ru -> en|one)$'), translate_ru)
translate_handler = MessageHandler(Filters.regex('^(de -> ru or ru->de|one)$'), translate_de)
translate_handler1 = MessageHandler(Filters.regex('^(es-> ru or ru ->es|one)$'), translate_es)
number_handler = MessageHandler(Filters.text, number)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(multiplication_handler)
dispatcher.add_handler(translate_handler)
dispatcher.add_handler(translate_handler1)
dispatcher.add_handler(number_handler)

updater.start_polling()
updater.idle()
