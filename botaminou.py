import os
os.system("pip install googletrans==3.1.0a0") 
from googletrans import Translator
import telebot,requests
import time

translator = Translator()
token = "5265441684:AAFG3QzdnnD4l3_5924C5lDgqd0O_soTaQg"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,"تم الأرسال بنجاح")
	
@bot.message_handler(func=lambda message:True)
def botrr(message):
	gg=translator.translate(message.text, src='ar',dest='en').text
	print(gg)
	url = "https://random-stuff-api.p.rapidapi.com/ai"
	querystring = {"msg":gg}
	headers = {
    'authorization': "WmmBekpAEOXL",
    'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
    'x-rapidapi-key': "ad66922befmshda45f4576d775a6p104cefjsn2db5c41c2477"
    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	gf=response.json()["AIResponse"]
	ad=gg=translator.translate(gf, src='en',dest='ar').text
	bot.send_message(message.chat.id,ad)
	
bot.polling(True)
	
