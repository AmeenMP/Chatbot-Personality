from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from openai import OpenAI

# Your bot's API token
API_TOKEN = config('API_TOKEN')

client = OpenAI(
    organization=config('ORGANIZATION'),
    project=config('PROJECT'),
    api_key=config('API_KEY')
)


def send_request(message):
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}]
    )
    return chat_completion


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am your Telegram bot.')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    print(update.message.text)
    reply = send_request(update.message.text)
    print(reply)
    await update.message.reply_text(reply.choices[0].message.content)


bot = ApplicationBuilder().token(API_TOKEN).build()
bot.add_handler(CommandHandler("start", handle_start))
bot.add_handler(MessageHandler(filters.TEXT, handle_message))

bot.run_polling()
