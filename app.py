from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('IYpF+56t7ZPEC+ogh3kQH6QNmRlU3mYHYzsBOAaMVqwOhj/61WAfLoOL9OewhYiES6x64uJAKzoiIpMHwV+BmUQ3y5Bc+UiaaLp115yvfyNpocm5Qj96rssmKiCJBxvRRe2zYkd8skglkT6DrgRf/AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a7231ff308a2d3fb7767588d7bdf54ca')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂你說什麼'

    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = r))


if __name__ == "__main__":
    app.run()