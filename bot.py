from decouple import config
from openai import OpenAI
from sqlalchemy.testing import db
from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
from db_connection import SessionLocal
from crud import create_user, get_user, create_message, get_messages

# Your bot's API token
API_TOKEN = config('API_TOKEN')

client = OpenAI(
    organization=config('ORGANIZATION'),
    project=config('PROJECT'),
    api_key=config('API_KEY')
)


def send_request(messages, last_prompt):
    payload = []
    if messages:
        for message in messages:
            payload.append({"role": "user", "content": message.prompt})
            payload.append({"role": "assistant", "content": message.reply})
    payload.append({"role": "user", "content": last_prompt})
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=payload
    )
    return chat_completion


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    data = {
        "first_name": first_name if first_name else "N/A",
        "last_name": last_name if last_name else "N/A",
        "telegram_user_id": update.message.from_user.id
    }
    try:
        with SessionLocal() as session:
            user = create_user(session, data)
            await update.message.reply_text(f"Hi {user.first_name}")
    except Exception as e:
        print(e)
        await update.message.reply_text(f"Error! try again")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        with SessionLocal() as session:
            user = get_user(session, update.message.from_user.id)
            messages = get_messages(session, user.id)

            reply = send_request(messages, update.message.text)
            reply_msg = reply.choices[0].message.content

            data = {
                "user_id": user.id,
                "prompt": update.message.text,
                "reply": reply_msg
            }
            message = create_message(session, data)
        await update.message.reply_text(reply_msg)
    except Exception as e:
        print(e)
        await update.message.reply_text(f"Error! try again")


def main():
    print("Starting bot...")
    bot = ApplicationBuilder().token(API_TOKEN).build()
    bot.add_handler(CommandHandler("start", handle_start))
    bot.add_handler(MessageHandler(filters.TEXT, handle_message))
    bot.run_polling()


if __name__ == "__main__":
    while True:
        main()
