from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import modul
from modul import *


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f'1.чтобы получить ответ на приветствие наберите /hello\n2.чтобы отсортировать послед на берите /sort а после него саму последовательность через пробел')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} ')


async def sort_process(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text

    res = msg[5:]

    res_par = res.split()

    sort_res = modul.qicksort(res_par)


    #list = [lambda i: int(i) for i in items], items
    await update.message.reply_text(f'Вы ввели последовательность {res_par}')
    await update.message.reply_text(f'Я Вам возвращаю последовательность упорядоченную по возрастанию {sort_res}')