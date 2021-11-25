from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.text & filters.private)
def echo(client, message):
    message.reply_text(message.text)


app.run()  # Automatically start() and idle()
