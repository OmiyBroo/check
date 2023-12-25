from pyrogram import Client, filters

bot = Client(
    "edupubbot",
    api_id = "21972339",
    api_hash = "614afcdbf45d6ba300ef320724a40de7",
    bot_token = "6807865279:AAEi9efKbeSL96nSCRrAXk9xCGiQAaxWpV8"
)

@bot.on_message(filters.command('start') & filters.private)
def startmsg(bot, message):
    bot.send_message(message.chat.id, "Hello there I am EduPub Bot /n/nI can Help Download Text Books In  1minute.")

    bot.run()
