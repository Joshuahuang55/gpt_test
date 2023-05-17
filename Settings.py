import os 
from linebot import LineBotApi, WebhookHandler
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

CHATGPT_API_KEY = os.getenv("OPENAI_API_KEY")