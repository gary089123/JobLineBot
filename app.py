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
    print ('User : ',event.source.user_id)
    reply = parse(event.message.text,event.source.user_id)

    for i in reply:

        line_bot_api.push_message(
            event.source.user_id,
            i)



def parse(string,user):
    text = string.split(",")
    ##############  系所  ##############
    if text[0] =='資電學院':
        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='系所',
                text='請選擇畢業系所',
                actions=[
                    MessageTemplateAction(
                        label='資工系',
                        text='資工系'
                    ),
                    MessageTemplateAction(
                        label='電機系',
                        text='電機系'
                    ),
                    MessageTemplateAction(
                        label='通訊系',
                        text='通訊系'
                    )
                ]
            )
        )
        return [response]
    elif text[0] =='工學學院':
        return [TextSendMessage(text='開發中')]
    elif text[0] =='理學院':
        return [TextSendMessage(text='開發中')]
    elif text[0] =='管理學院':
        return [TextSendMessage(text='開發中')]

    ##############  資工系  ##############

    elif text[0] == '資工系' and len(text)==1:
        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='職務類別',
                text='請選擇畢業系所',
                actions=[
                    MessageTemplateAction(
                        label='軟體設計工程師',
                        text='條件,2007001004'
                    ),
                    MessageTemplateAction(
                        label='韌體設計工程師',
                        text='條件,2007001005'
                    ),
                    MessageTemplateAction(
                        label='演算法開發工程師',
                        text='條件,2007001012'
                    ),
                    MessageTemplateAction(
                        label='更多',
                        text='more1'
                    )
                ]
            )
        )
        return [response]

    elif text[0] == 'more1':
        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='職務類別',
                text='請選擇職務類別',
                actions=[
                    MessageTemplateAction(
                        label='電玩程式設計師',
                        text='條件,2007001008'
                    ),
                    MessageTemplateAction(
                        label='資料庫管理人員',
                        text='條件,2007002002'
                    ),
                    MessageTemplateAction(
                        label='網路管理工程師',
                        text='條件,22007002005'
                    ),
                    MessageTemplateAction(
                        label='更多',
                        text='more2'
                    )
                ]
            )
        )
        return [response]

    elif text[0] == 'more2':
        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='職務類別',
                text='請選擇職務類別',
                actions=[
                    MessageTemplateAction(
                        label='MIS程式設計師',
                        text='條件,2007002003'
                    ),
                    MessageTemplateAction(
                        label='網路安全分析師',
                        text='條件,2007002008'
                    ),
                ]
            )
        )
        return [response]


    ##############  條件  ##############

    elif text[0] == '條件' and len(text)==2:

        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='身份類別',
                text='請選擇身份類別',
                actions=[
                    MessageTemplateAction(
                        label='不拘',
                        text= string+',0'
                    ),
                    MessageTemplateAction(
                        label='全職',
                        text= string+',1'
                    ),
                    MessageTemplateAction(
                        label='兼職',
                        text= string+',2'
                    ),
                ]
            )
        )
        return [response]

    elif text[0] == '條件' and len(text)==3:

        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='工作經驗',
                text='請選擇工作經驗',
                actions=[
                    MessageTemplateAction(
                        label='無工作經驗',
                        text= string+',-1'
                    ),
                    MessageTemplateAction(
                        label='未滿一年',
                        text= string+',0'
                    ),
                    MessageTemplateAction(
                        label='一年以上',
                        text= string+',1'
                    ),
                    MessageTemplateAction(
                        label='兩年以上',
                        text= string+',2'
                    )
                    
                ]
            )
        )
        return [response]

    elif text[0] == '條件' and len(text)==4:

        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='薪資',
                text='請選擇期望薪資(月薪)',
                actions=[
                    MessageTemplateAction(
                        label='不拘',
                        text= string+',X'
                    ),
                    MessageTemplateAction(
                        label='四萬以上',
                        text= string+',4'
                    ),
                    MessageTemplateAction(
                        label='五萬以上',
                        text= string+',5'
                    ),
                    MessageTemplateAction(
                        label='六萬以上',
                        text= string+',6'
                    )
                    
                ]
            )
        )
        return [response]
    
    ##############  學院  ##############
    elif text[0]=='hi':
        response = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='學院',
                text='請選擇畢業學院',
                actions=[
                    MessageTemplateAction(
                        label='資電學院',
                        text='資電學院'
                    ),
                    MessageTemplateAction(
                        label='工學院',
                        text='工學院'
                    ),
                    MessageTemplateAction(
                        label='理學院',
                        text='理學院'
                    ),
                    MessageTemplateAction(
                        label='管理學院',
                        text='管理學院'
                    )
                ]
            )
        )
        return [response]



    elif text[0] == '條件' and len(text)==5:
        data = searchjob(text)

        return [TextSendMessage(text='開發中')]


    elif text[0] == 'help':
        return [TextSendMessage(text='開發中'),TextSendMessage(text='開發中')]
    else:
        return [TextSendMessage(text='請以 \'hi\' 開始，更多使用方法請使用 \'help\'')]


        
def searchjob(text):
    import requests
    import json
    url = 'http://www.104.com.tw/i/apis/jobsearch.cfm?cat='+text[1]+'&role='+text[2]+'&fmt=8&order=1&cols=JOB,NAME,LINK,DESCRIPTION&exp='+text[3]
    if not text[4] == 'X':
        url = url+'&sltp=S&slmin='+text[4]+'0000'

    r = requests.get(url)

    jdata = r.json()

    print (jdata)
    data = jdata['data']
    for i in data:
        print( '職位名稱:',i["JOB"])
        print( '公司:',i["NAME"])
        print( '描述:',i["DESCRIPTION"])
        print( '網址:', i["LINK"])
        

    return data




import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)