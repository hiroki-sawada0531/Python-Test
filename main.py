# import config
from bs4 import BeautifulSoup
import requests
import urllib.request
import json
​
text = ''
aaaa = ''
count = 1
url = "https://www.pokemoncenter-online.com/?main_page=product_list&sort=new&cat1=card"
​
# URLにアクセス
request_html = urllib.request.urlopen(url)
soup_html = BeautifulSoup(request_html, "html.parser")
​
list_items = soup_html.find_all('li', class_='item')
​
for list_item in list_items:
    pokemon_item = list_item.find('p', class_='name').get_text()
    if count <= 7:
        text += str(count)
        text += '、'
        text += pokemon_item.strip()
        text += "\n"
        count += 1
    aaaa += pokemon_item
​
is_Eevee = 'イーブイ' in aaaa
​
if is_Eevee:
    webhook_url = "SlackのURL"
    slack_text = "<@ユーザーID> ポケットモンスターオンラインに、イーブイの商品が追加されたブイ。\n最新の商品一覧ブイよ。\n\n" + text + '\n\n' + url
    requests.post(webhook_url, data=json.dumps({
        "text" : slack_text,
        "icon_emoji" : ":eevee:",
        "username" : "ポケセンを監視するイーブイ"
    }))