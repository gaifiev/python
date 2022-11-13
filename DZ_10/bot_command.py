from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sympy


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}')
    name_user = update.message.text
    log = f'User request: {name_user}'
    wread_file(log)
    name_user1 = update.effective_user.first_name
    log1 = f'Hi, {name_user1}'
    wread_file(log1)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, my old friend! Составляю список команд:\n' +
                                    '/hello - привет\n' +
                                    '/help - список команд\n' +
                                    '/formula - арифметическое вычисление выражений.\nНапример: /formula 2+3+4^2/2-10')
    name_user2 = update.message.text
    log2 = f'User request: {name_user2}'
    wread_file(log2)


async def formula_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logirovanie = ''
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    j = sympy.Symbol('j')
    request = update.message.text
    logirovanie = f'User request: {request}'
    wread_file(logirovanie)
    items = request.partition('/formula ')[2]
    result = sympy.simplify(items)
    logirovanie = f'Result: {result}'
    wread_file(logirovanie)
    await update.message.reply_text(f'Result: {result}')


def wread_file(logirovanie):
    with open("D:\MyFirstPython\DZ_10\log.txt", "a") as write_file:
        write_file.write(logirovanie + '\n')
