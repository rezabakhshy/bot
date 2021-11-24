from pyrogram import Client,filters
import pytesseract
from PIL import Image 
from gtts import gTTS
import os
app = Client("my_accound",api_id=12721742,api_hash="2a81674bd5e1ccbaed8c07f898d614ca")

@app.on_message(filters.text & filters.me)
def media(client, message):
    text=message.text
    text2=text.split()[0]
    text=text.replace(text2,"")
     # Get bot results for "Fuzz Universe" from the inline bot @vid
    if text2=="!youvid":
        bot_results = app.get_inline_bot_results("vid",text)

        # Send the first result (bot_results.results[0]) to your own chat (Saved Messages)
        app.send_inline_bot_result("rezabz2", bot_results.query_id, bot_results.results[0].id)
    elif text2=="!youpic":
        bot_results = app.get_inline_bot_results("pic",text)

        # Send the first result (bot_results.results[0]) to your own chat (Saved Messages)
        app.send_inline_bot_result("rezabz2", bot_results.query_id, bot_results.results[0].id)
    elif text2=="!yougif":
        bot_results = app.get_inline_bot_results("gif",text)

        # Send the first result (bot_results.results[0]) to your own chat (Saved Messages)
        app.send_inline_bot_result("rezabz2", bot_results.query_id, bot_results.results[0].id)
    elif text2=="!ttr":
        language=text.split()[0]
        text=text.replace(language,"")
        myobj=gTTS(text=text,lang=language,slow=False)
        myobj.save("test.ogg")
        client.send_audio("me","test.ogg")
        os.remove('test.ogg')
app.run()  # Automatically start() and idle()