from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import modul
from modul import *


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f'1.чтобы получить ответ на приветствие наберите /hello\n2.чтобы отсортировать последовательность чисел наберите /sort а после него саму последовательность через пробел\n3.преобразовать десятичное число в двоичное наберите /binary и через пробел десятичное число')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} ')


async def sort_process(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text

    res = msg[5:]

    res_par = res.split()

    sort_res = modul.qicksort(res_par)



    await update.message.reply_text(f'Вы ввели последовательность {res_par}')
    await update.message.reply_text(f'Я Вам возвращаю последовательность упорядоченную по возрастанию {sort_res}')

async def dec_bin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text

    res = msg.split()
    decimal = int(res[-1])
    binar = modul.decimal_binary(decimal)
    await update.message.reply_text(f'введенное Вами число будет выглядеть в двоичной системе как {binar}')