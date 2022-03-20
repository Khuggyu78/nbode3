
import aminofix
import requests
import telebot
import time
c = aminofix.Client()

token = "5254908894:AAG1l7O8escxFe73Dwev9MhHAcKUmZ_1osE"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,"عايز ايه ؟")
	
@bot.message_handler(commands=['device'])
def start(message):
	a=requests.get("https://ka-generator.herokuapp.com/device").text
	bot.send_message(message.chat.id,a)
	
@bot.message_handler(commands=['id'])
def start(message):
	bot.send_message(message.chat.id,"يشيخ ارسل الرابط وفكنا من كلامك")
	
@bot.message_handler(func=lambda message:True)
def botrr(message):
	ch=message.text
	link = c.get_from_code(ch)
	comId = link.path[1:link.path.index("/")]
	chatId = link.objectId
	bot.send_message(message.chat.id,"comId= "+comId+"\n"+"chatId= "+chatId)
	
	
bot.polling(True)
print("done")	
