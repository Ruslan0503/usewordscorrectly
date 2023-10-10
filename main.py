from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,filters
import requests
from bs4 import BeautifulSoup



def finder(ss):
    url = "https://sentence.yourdictionary.com/{}".format(ss)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.findAll(class_="sentence-item__text")[:10]
    text = ""
    c = 1
    if(len(results))!=0:
        for i in results:
            text+=(str(c)+")"+i.text)+"\n"
            c+=1
    else:
        return "So'z topilmadi.."
    return text


async def hello(update:Update, context:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}\n Iltimos faqat bitta so'z kiriting")
    print(f"User {update.effective_user.first_name} entered..\n")

async def help(update:Update, context:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text(f"Botga biron inglizcha so'z yuboring")

async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Ishlanyapdi..\n")
    await update.message.reply_text(finder(update.message.text))

print('working..')
app = ApplicationBuilder().token('5898175331:AAG1HAaR571xa_M5__B4XmI2Zi7wCJZFATA').build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()