from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
import os
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))

def sendImageA(event):  #傳送圖片
    import  json, ssl, urllib.request

    url = 'https://pttbeauty168.zapto.org/api/images/random/'
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=context) as jsondata:
    #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
        data = json.loads(jsondata.read().decode('utf-8-sig')) 


    print(data['id'])
    print(data['Url'])


    try:
        
        message = ImageSendMessage(
            original_content_url = data['Url'],
            preview_image_url = data['Url']
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))