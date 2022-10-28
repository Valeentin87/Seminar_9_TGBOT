from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands_bot import*


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text('\n введите /help, чтобы узнать мои возможности')

app = ApplicationBuilder().token("5755386843:AAGY30CZhpH2bZZ-j5snOfG2HtkgKUdYvV0").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sort", sort_process))
app.add_handler(CommandHandler("binary", dec_bin))


print('server start')

app.run_polling()