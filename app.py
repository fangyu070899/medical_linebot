import os,json

from flask import Flask, abort, request, send_file

from src.fsm import TocMachine

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FlexSendMessage, BubbleContainer, ImageComponent,ImageSendMessage,QuickReply,QuickReplyButton,MessageAction

from utils.message import get_health_category_button ,get_category_button_2,get_category_button_3,get_symptom_category_button,get_diet_button,get_sport_button
from utils.quick_reply import get_heart_quick_reply,get_bone_quick_reply,get_brain_quick_reply,get_ear_quick_reply,get_elder_quick_reply,get_eye_quick_reply,get_female_quick_reply,get_gynecology_quick_reply,get_kidney_quick_reply,get_liver_quick_reply,get_lung_quick_reply,get_male_quick_reply,get_mind_quick_reply,get_minor_quick_reply,get_mouth_quick_reply,get_nutrition_quick_reply,get_skin_quick_reply,get_stomach_quick_reply,get_urinaty_quick_reply,get_quick_reply
from utils.url_crawler import search_discription,search_paper

app = Flask(__name__)

# line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
# handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))

line_bot_api = LineBotApi("CHANNEL_ACCESS_TOKEN")
handler = WebhookHandler("CHANNEL_SECRET")

machine = TocMachine(
    states=[
        "user",
        "searched_term",
        "suggest_term",
        "symptom_category",
        "nutrition_category",
        "diet_category",
        "sport_category",
        "disease_category",
        "disease_category2",
        "disease",
        "symptom"
        ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "suggest_term",
            "conditions": "is_going_to_suggest_term",
        },
        {
            "trigger": "advance",
            "source": "searched_term",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {
            "trigger": "advance",
            "source": "suggest_term",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "disease_category",
            "conditions": "is_going_to_disease_category",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "symptom_category",
            "conditions": "is_going_to_symptom_category",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "diet_category",
            "conditions": "is_going_to_diet_category",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "sport_category",
            "conditions": "is_going_to_sport_category",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "nutrition_category",
            "conditions": "is_going_to_nutrition_category",
        },
        {
            "trigger": "advance",
            "source": "disease_category",
            "dest": "disease_category2",
            "conditions": "is_going_to_disease_category2",
        },
        {
            "trigger": "advance",
            "source": "disease_category2",
            "dest": "disease",
            "conditions": "is_going_to_disease",
        },
        {
            "trigger": "advance",
            "source": "disease",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {
            "trigger": "advance",
            "source": "disease",
            "dest": "suggest_term",
            "conditions": "is_going_to_suggest_term",
        },
        {
            "trigger": "advance",
            "source": "symptom_category",
            "dest": "symptom",
            "conditions": "is_going_to_symptom",
        },
        {
            "trigger": "advance",
            "source": "symptom",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {
            "trigger": "advance",
            "source": "symptom",
            "dest": "suggest_term",
            "conditions": "is_going_to_suggest_term",
        },
        {
            "trigger": "advance",
            "source": "nutrition_category",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {
            "trigger": "advance",
            "source": "nutrition_category",
            "dest": "suggest_term",
            "conditions": "is_going_to_suggest_term",
        },
        {
            "trigger": "advance",
            "source": "diet_category",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {
            "trigger": "advance",
            "source": "sport_category",
            "dest": "searched_term",
            "conditions": "is_going_to_searched_term",
        },
        {"trigger": "go_back", "source": ["searched_term", "suggest_term", "symptom_category", "nutrition_category", "diet_category", "sport_category", "disease_category"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)



def reply_rich_menu(get_message,reply_token):
    if get_message=="????????????" :
        message=[
            FlexSendMessage(alt_text='?????????????????????????',contents=get_health_category_button()),
            TextSendMessage(text=f"??????????????????????????????????????????????????????????????????????????????????????????????????????"),
        ]
        line_bot_api.reply_message(reply_token,message)
    elif get_message=="????????????":
        message=[
            FlexSendMessage(alt_text='?????????????????????????',contents=get_symptom_category_button()),
            TextSendMessage(text=f"??????????????????????????????????????????????????????????????????????????????????????????????????????"),
        ]
        line_bot_api.reply_message(reply_token,message)
    elif get_message=="????????????":
        message=[
            TextSendMessage(text=f"??????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/fbgvaDD.png','https://i.imgur.com/fbgvaDD.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_nutrition_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="????????????":
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='???????????????????????????????',contents=get_sport_button()))
    elif get_message=="????????????":
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='???????????????????????????????',contents=get_diet_button()))
    else :
        reply = TextSendMessage(text=f"?????????????????????????????????")
        line_bot_api.reply_message(reply_token, reply)
    
def reply_category(get_message,reply_token):
    if get_message=="?????? ?????? ?????? ?????? ??????" :
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='?????????????????????????',contents=get_category_button_3("??????","??????","??????")))
    elif get_message=="?????? ?????? ?????? ?????? ??????" :
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='?????????????????????????',contents=get_category_button_2("??????","???????????????")))  
    elif get_message=="?????? ?????? ????????? ??????" :
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='?????????????????????????',contents=get_category_button_2("??????","?????????")))  
    elif get_message=="?????? ??? ??? ??? ??? ??????" :
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='?????????????????????????',contents=get_category_button_2("??????","?????????")))
    elif get_message=="?????? ??? ?????? ?????? ??????" :
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='?????????????????????????',contents=get_category_button_2("????????????","??????")))  
    elif get_message=="?????? ?????? ????????? ?????? ??????" :
        line_bot_api.reply_message(reply_token,FlexSendMessage(alt_text='?????????????????????????',contents=get_category_button_3("??????","?????????","??????"))) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/2o4Sk91.png','https://i.imgur.com/2o4Sk91.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_heart_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/xgYKPfR.png','https://i.imgur.com/xgYKPfR.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_liver_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/rlFfG3q.png','https://i.imgur.com/rlFfG3q.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_lung_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/d8MOwVE.png','https://i.imgur.com/d8MOwVE.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_stomach_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ??????????????? ??????" :
        message=[
            TextSendMessage(text=f"??????????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/uKXwmvo.png','https://i.imgur.com/uKXwmvo.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_mouth_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/pNoryEo.png','https://i.imgur.com/pNoryEo.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_kidney_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ????????? ??????" :
        message=[
            TextSendMessage(text=f"????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/FnbWLRG.png','https://i.imgur.com/FnbWLRG.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_urinaty_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/rWkx9TO.png','https://i.imgur.com/rWkx9TO.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_eye_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ????????? ??????" :
        message=[
            TextSendMessage(text=f"????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/lUlXcqL.png','https://i.imgur.com/lUlXcqL.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_ear_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ???????????? ??????" :
        message=[
            TextSendMessage(text=f"???????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/mxsj6Sz.png','https://i.imgur.com/mxsj6Sz.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_bone_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/44QpZus.png','https://i.imgur.com/44QpZus.png'),
            ImageSendMessage('https://i.imgur.com/GtlkT25.png','https://i.imgur.com/GtlkT25.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_skin_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/m53sr8b.png','https://i.imgur.com/m53sr8b.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_mind_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ????????? ??????" :
        message=[
            TextSendMessage(text=f"????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/9bzpHIX.png','https://i.imgur.com/9bzpHIX.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_brain_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/xH68mfS.png','https://i.imgur.com/xH68mfS.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_gynecology_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/UFTgtoo.png','https://i.imgur.com/UFTgtoo.png'),
            ImageSendMessage('https://i.imgur.com/9njxXZ4.png','https://i.imgur.com/9njxXZ4.png'),
            ImageSendMessage('https://i.imgur.com/GEi54o2.png','https://i.imgur.com/GEi54o2.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_male_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/VZpmDEp.png','https://i.imgur.com/VZpmDEp.png'),
            ImageSendMessage('https://i.imgur.com/248ZgU7.png','https://i.imgur.com/248ZgU7.png'),
            ImageSendMessage('https://i.imgur.com/dCSBNeY.png','https://i.imgur.com/dCSBNeY.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_female_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"?????????????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/km1gFjV.png','https://i.imgur.com/km1gFjV.png'),
            ImageSendMessage('https://i.imgur.com/04SeZyc.png','https://i.imgur.com/04SeZyc.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_elder_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    elif get_message=="?????? ?????? ??????" :
        message=[
            TextSendMessage(text=f"???????????????????????????????????????"),
            ImageSendMessage('https://i.imgur.com/vp4WXHk.png','https://i.imgur.com/vp4WXHk.png'),
            TextSendMessage(text=f"???????????????????????????????????????",quick_reply=get_minor_quick_reply()),
        ]
        line_bot_api.reply_message(reply_token,message) 
    else :
        reply = TextSendMessage(text=f"?????????????????????????????????")
        line_bot_api.reply_message(reply_token, reply)

def reply_discription(get_message,reply_token):
    with open("utils/categories/url.json",'r',encoding='utf-8') as j:
        json_file=json.load(j)
    num=0
    item=[]
    for j in json_file['url']:
        if(get_message==j['name']):
            reply = search_discription(j['name'],j['url'])
            message=reply[0]
            if(reply[1] != []):
                print(reply[1])
                message.append(TextSendMessage(text=f"??????{get_message}?????????????????????????",quick_reply=get_quick_reply(reply[1])))
            line_bot_api.reply_message(reply_token, message)
            return
        elif(get_message in j['name'] and num<13):
            if(len(j['name'])>20):continue
            item.append( 
                QuickReplyButton(
                       action=MessageAction(label=j['name'], text=j['name'])
                   ))
            num+=1
    if(num==0):
        reply = TextSendMessage(text=f"?????????????????????????????????")
        line_bot_api.reply_message(reply_token, reply)
    else:
        message=[
            TextSendMessage(text=f"?????????????????????????????????????????????????"),
            TextSendMessage(text=f"??????????????????????????????????????????",quick_reply=get_quick_reply(item)),
        ]
        line_bot_api.reply_message(reply_token, message)

def reply_paper(get_message,reply_token):
    title=get_message.split('->')[0]
    print(title)
    category=get_message.split('->')[1]
    print(category)
    with open("utils/categories/url.json",'r',encoding='utf-8') as j:
        json_file=json.load(j)
    for j in json_file['url']:
        if(title==j['name']):
            reply = search_paper(j['name'],category,j['url'])
            message=reply[0]
            if(reply[1] != []):
                message.append(TextSendMessage(text=f"??????{title}?????????????????????????",quick_reply=get_quick_reply(reply[1])))
            # print(message)
            line_bot_api.reply_message(reply_token, message)
            return
    reply = TextSendMessage(text=f"?????????????????????????????????")
    line_bot_api.reply_message(reply_token, reply)

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


@app.route("/show_fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    get_message = event.message.text
    reply_token = event.reply_token


    if "??????" in get_message :
        reply_rich_menu(get_message,reply_token)
    elif "??????" in get_message and "??????" in get_message :
        reply_category(get_message,reply_token)
    elif "->" in get_message :
        reply_paper(get_message,reply_token)
    else :
        reply_discription(get_message,reply_token)

if __name__ == "__main__":
    app.run(debug=True,port=8000)