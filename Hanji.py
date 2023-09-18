from telegram.ext import CommandHandler, updater, MessageHandler, Filters
from deep_translator import GoogleTranslator
from langdetect import detect

Token = '6342917337:AAGn42lBVdEz6xL9RWQJHyFL_b4kLxeCohU'

updater = updater.Updater(Token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("""Welcome to Hanji Bot!
                              به هانجی خوش اومدی!""")

def help(update, context):
    update.message.reply_text("""
/start -> Welcome to Hanji!
به هانجی خوش اومدی!

/help -> A brief introduction (This message)
یه معرفی مختصر (این پیام)

You can send any message in Enlish or Persian that you like and I will translate it for you!
هر پیام انگلیسی یا فارسی‌ای رو که دوست داشته باشی میتونی برام بفرستی و من برات ترجمه‌ش میکنم!

Much Easier than you think ;)
خیلی ساده‌تر از چیزی که فکر میکنی ;)

One thing you need to know: for using me in groups put / and a space at the begining of your text!
یه نکته دیگه رو که باید بهت بگم اینه که اگه میخوای ازم توی گروه استفاده کنی یه  / و بعد از اون یه فاصله بذار تا کار رو برات انجام بدم!
""")

def translator(update, context):
    text = update.message.text
    if detect(text) == 'en':
        translated = GoogleTranslator(source='en', target='fa').translate(text)
        update.message.reply_text(translated)
    else:
        translated = GoogleTranslator(source='fa', target='en').translate(text)
        update.message.reply_text(translated)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.text, translator))


updater.start_polling()
updater.idle()