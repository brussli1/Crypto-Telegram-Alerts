from flask import Flask, request, jsonify
import telegram
import os

app = Flask(__name__)
bot = telegram.Bot(token=os.environ.get("TELEGRAM_TOKEN"))

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/telegram", methods=["POST"])
def handle_telegram_update():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat_id
    text = update.message.text

    if text == "/start":
        bot.sendMessage(chat_id=chat_id, text="Welcome to the bot!")
    else:
        bot.sendMessage(chat_id=chat_id, text=f"You said: {text}")

    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
