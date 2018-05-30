from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,
    PostbackTemplateAction,ButtonsTemplate,URITemplateAction,MessageTemplateAction
)

app = Flask(__name__)

line_bot_api = LineBotApi('o2xY5OiKwx/3WioastnjkAvXN2qTin/RVUdm6n8Q6RCDvnPRACs1gxZkhkJtPvhpeXoz3U8p5uXl2sFY699/o83FlR7NDlDVtcbtj86FEAMILq8FpQdDQdSI/HlraxHeBHDePmTab29hZc/xvDwsXwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dc34c9fbeef195c821b30173bac3632d')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    reply = parse(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        reply)


def parse(text):

    ##############  學院  ##############
    if text =='資電學院':
        return 0
    elif text =='工學學院':
        return 0
    elif text =='理學院':
        return 0
    elif text =='管理學院':
        return 0
    elif text =='文學院':
        return 0
    else:
        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='學院',
                text='請選擇畢業學院',
                actions=[
                    MessageTemplateAction(
                        label='資電學院',
                        text='資電學院'
                    )
                ]
            )
        )
        return response

        





import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)