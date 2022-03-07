import requests
from telebot import types
import telebot
from time import sleep
import random
import time
token = "5218688832:AAFEDBG9Udpd_XSiZ470dSBQlp50L00FCjg"
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="- بوت القران",url="https://t.me/Qxurbot")
ge = types.InlineKeyboardButton(text ="ألمانيا",callback_data = 'e')


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co,ge)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
Covid -19 staute Germany
- - - - - - - - - - 
By  : @O4mrrr
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
    
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'e':
    	re(call.message)
def re(message):
		time.sleep(5)
		bot.send_message(message.chat.id,"<strong>Executed..... </strong>",parse_mode="html")
		url =f"https://coronavirus-19-api.herokuapp.com/countries/iraq"
		stats = requests.get(url)
		json_stats = stats.json()
		country = json_stats["country"]
		totalCases = json_stats["cases"]
		todayCases = json_stats["todayCases"]
		totalDeaths = json_stats["deaths"]
		todayDeaths = json_stats["todayDeaths"]
		recovered = json_stats["recovered"]
		active = json_stats["active"]
		critical = json_stats["critical"]
		casesPerOneMillion =json_stats["casesPerOneMillion"]
		deathsPerOneMillion = json_stats["deathsPerOneMillion"]
		totalTests = json_stats["totalTests"]
		testsPerOneMillion =json_stats["testsPerOneMillion"]
		msge = f"""
—أحصائيات كورونا في ألمانيا!
—مجموع الحالات : {totalCases}
—حالات اليوم : {todayCases}
—مجموع الوفيات : {totalDeaths}
—وفيات اليوم : {todayDeaths}
—المسترجع : {recovered}
—نشط : {active}
—الحالات الحرجة : {critical}
—حالات لكل مليون : {casesPerOneMillion}
—الوفيات لكل مليون : {deathsPerOneMillion}
—مجموع الاختبارات : {totalTests}
—الاختبارات لكل مليون : {testsPerOneMillion}
"""
		bot.send_message(message.chat.id,msge)
		
		
    
pass
bot.polling(True)
