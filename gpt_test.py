#from flask_ngrok import run_with_ngrok   # colab 使用，本機環境請刪除
from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('jMYrhi8gzzBrVI0UsBTtiIPrhxlfni+Nm9/Eha4BYCGm+Q/Gtt+1IRAk9e84ab86lirHm90fA+gof29efTqLfrTw7sKAlAziiN5tHI2PfoZe2qDsbcjimNUMcwOxV3grsF0xGLg9wyM1dOZf/NVlzwdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('6f37b50462a4bdfb96e40152eb58c193')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        # 取出文字的前五個字元，轉換成小寫
        ai_msg = msg[:6].lower()
        reply_msg = ''
        # 取出文字的前五個字元是 hi ai:
        if ai_msg == 'hi ai:':
            openai.api_key = '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'
            # 將第六個字元之後的訊息發送給 OpenAI
            response = openai.Completion.create(
                model='text-davinci-003',
                prompt=msg[6:],
                max_tokens=256,
                temperature=0.5,
                )
            # 接收到回覆訊息後，移除換行符號
            reply_msg = response["choices"][0]["text"].replace('\n','')
        else:
            reply_msg = msg
        text_message = TextSendMessage(text=reply_msg)
        line_bot_api.reply_message(tk,text_message)
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    run_with_ngrok(app)   # colab 使用，本機環境請刪除
    app.run()