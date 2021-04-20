#Import everything you need
from telegram.ext import Updater, CommandHandler
import random
import os
import logging

#start the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#Replace with the token that BotFather gives you
TOKEN = 'Your Token'

#this is the port for the webhook
PORT = int(os.environ.get('PORT', 80))

#these are the lists from which the bot randomly choose after your command
lista_hype = ['Che figata!', 'Cazzo durissimo', 'Meglio di Mass Effect', 'Godzilla!', 'Raga ho scaricato la demo di un gioco fighissimo multiplayer tipo Mass Effect']
lista_ecodado = ['IL CESTINO!', 'Usa il posacenere', 'Cazzo lo butti nella carta se è plastica']
lista_lol = ['Lollai durissimo', 'LOL', 'AHHAHAHHAHHAHHAHAH']
lista_lavoro = ['Figa raga proprio stasera, ho un turno di merda', 'No raga sono a pezzi dal lavoro',
                'Minchia raga non possiamo fare domani sera? Faccio notte']

#this is the basic function to implement the random sending of images
def pic(update, context):
    bot = telegram.Bot(token=TOKEN)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=open("file\image.jpg", 'rb'))

#this randomly selects from ALL the lists
def a_caso(update, context):
    update.message.reply_text(random.choice(lista_lavoro + lista_hype + lista_ecodado + lista_lol))

#here there are the functions differenciated for every command

def hype(update, context):
    update.message.reply_text(random.choice(lista_hype))

def lol(update, context):
    update.message.reply_text(random.choice(lista_lol))

def lavoro(update, context):
    update.message.reply_text(random.choice(lista_lavoro))

def ecodado(update, context):
    update.message.reply_text(random.choice(lista_ecodado))

#this is to return the error log
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

    
def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
#these are the command handlers
    dp.add_handler(CommandHandler("hype", hype))
    dp.add_handler(CommandHandler("lol", lol))
    dp.add_handler(CommandHandler("lavoro", lavoro))
    dp.add_handler(CommandHandler("ecodado", ecodado))
    dp.add_handler(CommandHandler("Random", a_caso))
    dp.add_handler(CommandHandler("Pic", pic))

    dp.add_error_handler(error)

#this is the part where it connects to heroku for the deployment
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url='https://APPNAME.herokuapp.com/' + TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()
