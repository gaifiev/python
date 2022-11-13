#  Прикрутить бота к задачам с предыдущего семинара:
#  Создать калькулятор для работы с рациональными и
#  комплексными числами, организовать меню, добавив в неё систему логирования

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *
import settings


app = ApplicationBuilder().token(settings.API_KEY).build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("formula", formula_command))

print('Сервер запущен')
app.run_polling()
