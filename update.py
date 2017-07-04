
import requests
# import sendemail
from lxml import etree


shadowsocks_url = 'https://github.com/shadowsocks/shadowsocks-windows/releases'
shadowsocks_path = '//div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/h1/a/text()'

gfwlist_url = 'https://github.com/gfwlist/gfwlist/commits/master/gfwlist.txt'
gfwlist_path = '//div[2]/div[1]/div[2]/ol[1]/li[1]/div[2]/p/a/text()'

potplayer_url = 'https://potplayer.daum.net/'
potplayer_path = '//div[@class="update_version fst"]/strong/text()'

office_url = 'https://technet.microsoft.com/en-us/office/mt465751.aspx'
office_path = '//div[1]/div[1]/div[1]/h4/text()[2]'

chrome_url = 'https://windowsforum.com/resources/google-chrome.9/history'
chrome_path = '//tr[@class="dataRow  "][1]/td[1]/text()'

def update(url, path):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
	html = requests.get(url,headers = headers)
	selector = etree.HTML(html.text)
	texts = selector.xpath(path)
	for text in texts:
		return text

if __name__ == '__main__':

	shadowsocks = update(shadowsocks_url, shadowsocks_path)
	gfwlist = update(gfwlist_url, gfwlist_path)
	potplayer = update(potplayer_url, potplayer_path)
	office = update(office_url, office_path)
	chrome = update(chrome_url, chrome_path)

	output = open('update.txt','r')
	if shadowsocks+'\n' != output.readline():
		sendemail.send_email('Shadowsocks更新到啦！\n最新版本/时间： '+shadowsocks)
	if gfwlist+'\n' != output.readline():
		sendemail.send_email('GFWList更新到啦！\n最新版本/时间： '+gfwlist)
	if potplayer+'\n' != output.readline():
		sendemail.send_email('Potplayer更新到啦！\n最新版本/时间： '+potplayer)
	if office+'\n' != output.readline():
		sendemail.send_email('Office更新到啦！\n最新版本/时间： '+office)
	if chrome+'\n' != output.readline():
		sendemail.send_email('Chrome更新到啦！\n最新版本/时间： '+chrome)
	output.close()

	output = open('update.txt','w')
	output.write(shadowsocks+'\n')
	output.write(gfwlist+'\n')
	output.write(potplayer+'\n')
	output.write(office+'\n')
	output.write(chrome+'\n')
	output.close()
	
