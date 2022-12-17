import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FlexSendMessage, BubbleContainer, ImageComponent

from utils.message import get_health_category_button

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    if get_message=="健康百科" :
        line_bot_api.reply_message(event.reply_token,FlexSendMessage(alt_text="你可以選擇分類，來查找相關的病症清單，或直接告訴我你想查詢的病症名稱", contents=get_health_category_button()))
    
    else :
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token, reply)

