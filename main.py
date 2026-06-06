import os

from telegram import (
    ReplyKeyboardMarkup,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

keyboard = [
    ["Настроение", "Сон"],
    ["Таблетки", "Музыка"],
    ["Поговорить", "Мини-игры"]
]

menu = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "приветусики 🌙\nя рядом. выбери кнопку:",
        reply_markup=menu
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Настроение":
        await update.message.reply_text(
            "как ты себя чувствуешь?"
        )

    elif text == "Сон":
        await update.message.reply_text(
            "что снилось?"
        )

    elif text == "Таблетки":

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "✅ Выпила",
                    callback_data="pills_taken"
                )
            ],
            [
                InlineKeyboardButton(
                    "💤 Сегодня не нужно",
                    callback_data="pills_skip_day"
                )
            ]
        ])

        await update.message.reply_text(
            "💊 время таблеток",
            reply_markup=buttons
        )

    elif text == "Музыка":
        await update.message.reply_text(
            "🎧 сегодня тебе подходит что-то странное и ночное"
        )

    elif text == "Поговорить":
        await update.message.reply_text(
            "я слушаю 🌙"
        )

    elif text == "Мини-игры":
        await update.message.reply_text(
            "🎮 пока не готово"
        )

    else:
        await update.message.reply_text(
            "я тебя услышал"
        )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    if query.data == "pills_taken":
        await query.message.reply_text(
            "умничка 🫶"
        )

    elif query.data == "pills_skip_day":
        await query.message.reply_text(
            "хорошо 🌙"
        )

print("бот запущен 🌙")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        message
    )
)

app.add_handler(
    CallbackQueryHandler(buttons)
)

app.run_polling()
