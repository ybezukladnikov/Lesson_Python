from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5647026158:AAHSap2UcNZoqwqUGG1uPMgS1hqRed0jrZ8").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()


# import matplotlib.pyplot as plt
# import numpy as np
#
# list_m = [1,2,34,5,3,2]
# plt.plot(list_m)
#
# plt.show()
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

