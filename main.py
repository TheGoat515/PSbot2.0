from config import BOT_TOKEN
import logging

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
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
        fr'Hi {user.mention_markdown_v2()}\!', )


def help(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        'Help not available yet, good luck', )


def paradestate(update: Update, context: CallbackContext) -> None:
    global Totalstrength, Currentstrength, JurongCstrength, JurongTstrength, JurongLVE, JurongOFF, JurongMC, JurongOS, JurongAO, JurongOthers
    global JurongRSO, JurongRSI, JurongCourse, JurongMA
    global JLVE, JOFF, JMC, JOS, JAO, JOTHERS, JCourse, JMA, JRSO, JRSI
    Totalstrength = 0
    Currentstrength = 0
    JurongCstrength = 0
    JurongTstrength = 0
    JurongLVE = 0
    JurongOFF = 0
    JurongMC = 0
    JurongOS = 0
    JurongAO = 0
    JurongOthers = 0
    JurongRSO = 0
    JurongRSI = 0
    JurongCourse = 0
    JurongMA = 0
    JLVE = ""
    JOFF = ""
    JMC = ""
    JMA = ""
    JRSO = ""
    JRSI = ""
    JOS = ""
    JAO = ""
    JCourse = ""
    JOTHERS = ""

    """Send a message when the command /ps is issued."""
    user = update.effective_user
    keyboard = [
        [
            InlineKeyboardButton("Off", callback_data='Off'),
            InlineKeyboardButton("Leave", callback_data='Leave'),
        ],
        [InlineKeyboardButton("MC", callback_data='MC'),
         InlineKeyboardButton("MA", callback_data="MA"),
         ],
        [
            InlineKeyboardButton("RSO", callback_data="RSO"),
            InlineKeyboardButton("RSI", callback_data="RSI")
        ],
        [
            InlineKeyboardButton("AO", callback_data="AO"),
            InlineKeyboardButton("OS", callback_data="OS")
        ],
        [
            InlineKeyboardButton("CSE", callback_data="Course"),
            InlineKeyboardButton("Others", callback_data="Others")
        ],
        [
            InlineKeyboardButton("Present", callback_data="Present")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if JurongLVE != 0:
        JLVE = fr'LVE:{JurongLVE}' + '\n'
    if JurongOFF != 0:
        JOFF = fr'OFF:{JurongOFF}' + '\n'
    if JurongMC != 0:
        JMC = fr'MC:{JurongMC}' + '\n'
    if JurongMA != 0:
        JMA = fr'MA:{JurongMA}' + '\n'
    if JurongOS != 0:
        JOS = fr'OS:{JurongOS}' + '\n'
    if JurongAO != 0:
        JAO = fr'AO:{JurongAO}' + '\n'
    if JurongRSO != 0:
        JRSO = fr'RSO:{JurongRSO}' + '\n'
    if JurongRSI != 0:
        JRSI = fr'RSI:{JurongRSI}' + '\n'
    if JurongCourse != 0:
        JCourse = fr'CSE:{JurongCourse}' + '\n'
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
        fr'{JRSO}'
        fr'{JRSI}'
        fr'{JMA}'
        fr'{JMC}'
        fr'{JOS}'
        fr'{JAO}'
        fr'{JCourse}'
        fr'{JOTHERS}'
        '\n'
        '<b>HQ</b>' '\n'
        '\n' '<b>Section 1</b>' '\n'
        '\n' '<b>Section 2</b>' '\n'
        '\n' '<b>Section 3</b>', reply_markup=reply_markup

    )


def paradestateEdit(update: Update, context: CallbackContext, ) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    global Totalstrength, Currentstrength, JurongCstrength, JurongTstrength, JurongLVE, JurongOFF, JurongMC, JurongOS, JurongAO, JurongOthers
    global JurongRSO, JurongRSI, JurongCourse, JurongMA
    global JLVE, JOFF, JMC, JOS, JAO, JOTHERS, JCourse, JMA, JRSO, JRSI

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery

    keyboard = [
        [
            InlineKeyboardButton("Off", callback_data='Off'),
            InlineKeyboardButton("Leave", callback_data='Leave'),
        ],
        [InlineKeyboardButton("MC", callback_data='MC'),
         InlineKeyboardButton("MA", callback_data="MA"),
         ],
        [
            InlineKeyboardButton("RSO", callback_data="RSO"),
            InlineKeyboardButton("RSI", callback_data="RSI")
        ],
        [
            InlineKeyboardButton("AO", callback_data="AO"),
            InlineKeyboardButton("OS", callback_data="OS")
        ],
        [
            InlineKeyboardButton("CSE", callback_data="Course"),
            InlineKeyboardButton("Others", callback_data="Others")
        ],
        [
            InlineKeyboardButton("Present", callback_data="Present")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.answer()
    if query.data == "Present":
        JurongCstrength += 1
    if query.data == "Leave":
        JurongLVE += 1
    if query.data == "Off":
        JurongOFF += 1
    if query.data == "MC":
        JurongMC += 1
    if query.data == "MA":
        JurongMA += 1
    if query.data == "RSO":
        JurongRSO += 1
    if query.data == "RSI":
        JurongRSI += 1
    if query.data == "AO":
        JurongAO += 1
    if query.data == "OS":
        JurongOS += 1
    if query.data == "Course":
        JurongCourse += 1
    if query.data == "Others":
        JurongOthers += 1
    if JurongLVE != 0:
        JLVE = fr'LVE:{JurongLVE}' + '\n'
    if JurongOFF != 0:
        JOFF = fr'OFF:{JurongOFF}' + '\n'
    if JurongMC != 0:
        JMC = fr'MC:{JurongMC}' + '\n'
    if JurongMA != 0:
        JMA = fr'MA:{JurongMA}' + '\n'
    if JurongOS != 0:
        JOS = fr'OS:{JurongOS}' + '\n'
    if JurongAO != 0:
        JAO = fr'AO:{JurongAO}' + '\n'
    if JurongRSO != 0:
        JRSO = fr'RSO:{JurongRSO}' + '\n'
    if JurongRSI != 0:
        JRSI = fr'RSI:{JurongRSI}' + '\n'
    if JurongCourse != 0:
        JCourse = fr'CSE:{JurongCourse}' + '\n'
    if JurongOthers != 0:
        JOTHERS = fr'Others:{JurongOthers}' + '\n'
    query.edit_message_text(

        fr'<b>31FMD Parade State - {today} </b>' '\n' '\n'
        fr'Total Strength: {Totalstrength}' '\n'
        fr'Current Strength: {Currentstrength}' '\n' '\n'
        '----------------------------------' '\n'
        fr'Jurong Total Strength: {JurongTstrength}' '\n'
        fr'Jurong Current Strength: {JurongCstrength}' '\n' '\n'
        fr'{JLVE}'
        fr'{JOFF}'
        fr'{JRSO}'
        fr'{JRSI}'
        fr'{JMA}'
        fr'{JMC}'
        fr'{JOS}'
        fr'{JAO}'
        fr'{JCourse}'
        fr'{JOTHERS}'
        '\n'
        '<b>HQ</b>' '\n'
        '\n' '<b>Section 1</b>' '\n'
        '\n' '<b>Section 2</b>' '\n'
        '\n' '<b>Section 3</b>', parse_mode='HTML', reply_markup=reply_markup

    )


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
    dispatcher.add_handler(CallbackQueryHandler(paradestateEdit))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
