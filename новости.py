import requests
from bs4 import BeautifulSoup as bs
import time
import telebot

def novosty():
	page = requests.get('https://rg.ru/news.html')
	soup = bs(page.text,"html.parser")
	news = soup.find('a',class_ = 'ItemOfListStandard_title__eX0Jw').text
	return news

bot = telebot.TeleBot("5853217953:AAFKFERQ59Za5mwrcBtcnrifpwKwHeaSJuM")

@bot.message_handler()
def send_welcome(message):
	while True:
		bot.send_message(-1001252386646,novosty())
		time.sleep(480)

	
bot.infinity_polling()