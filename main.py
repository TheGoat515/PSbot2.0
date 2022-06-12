from config import BOT_TOKEN
import logging

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, ContextTypes
from datetime import date

today = date.today()
today = str(today)
today = today.split("-")
dateorder = [2, 1, 0]
today = [today[i] for i in dateorder]
today = ''.join(today)
print(today)
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',)

def help(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        'Help not available yet, good luck',)


def paradestate(update: Update, context: CallbackContext) -> None:
    JLVE=""
    JOFF=""
    JMC=""
    JOS=""
    JAO=""
    JOTHERS=""
    Totalstrength = 0
    Currentstrength = 0
    JurongCstrength = 0
    JurongTstrength = 0
    JurongLVE = 2
    JurongOFF = 5
    JurongMC = 2
    JurongOS = 0
    JurongAO = 1
    JurongOthers= 3

    """Send a message when the command /ps is issued."""
    user = update.effective_user
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if JurongLVE != 0:
        JLVE = fr'LVE:{JurongLVE}' + '\n'
    if JurongOFF != 0:
        JOFF = fr'OFF:{JurongOFF}' + '\n'
    if JurongMC != 0:
        JMC = fr'MC:{JurongMC}' + '\n'
    if JurongOS != 0:
        JOS = fr'OS:{JurongOS}' + '\n'
    if JurongAO != 0:
        JAO = fr'AO:{JurongAO}' + '\n'
    if JurongOthers != 0:
        JOTHERS = fr'Others:{JurongOthers}' + '\n'
    update.message.reply_html(
        fr'<b>31FMD Parade State - {today} </b>' '\n' '\n'
        fr'Total Strength: {Totalstrength}' '\n'
        fr'Current Strength: {Currentstrength}' '\n' '\n'
        '----------------------------------' '\n'
        fr'Jurong Total Strength: {JurongTstrength}' '\n'
        fr'Jurong Current Strength: {JurongCstrength}' '\n' '\n'
        fr'{JLVE}'
        fr'{JOFF}'
        fr'{JMC}'
        fr'{JOS}'
        fr'{JAO}'
        fr'{JOTHERS}'
        '\n'
        '<b>HQ</b>' '\n'
        '\n' '<b>Section 1</b>' '\n'
        '\n' '<b>Section 2</b>' '\n'
        '\n' '<b>Section 3</b>' , reply_markup=reply_markup
    )

def buttontest(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
 
    update.message.reply_text("Please choose:", )

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ps", paradestate))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("button",buttontest))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
