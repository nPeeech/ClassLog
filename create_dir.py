import os
import datetime
import shutil
from bs4 import BeautifulSoup
from bs4 import Tag

#今日のディレクトリを作成
os.makedirs("/home/pi/mnt/Class_Log/" + datetime.datetime.today().strftime("%Y_%m_%d"))

wkday = datetime.date.today().weekday()
today = datetime.datetime.today().strftime("%Y_%m_%d")

#テンプレートHTMLをコピーして今日のディレクトリに配置
if wkday == 0:
    shutil.copyfile("/home/pi/mnt/Class_Log/template/MON.html","/home/pi/mnt/Class_Log/" + today + "/main.html")
elif wkday == 1:
    shutil.copyfile("/home/pi/mnt/Class_Log/template/TUE.html","/home/pi/mnt/Class_Log/" + today + "/main.html")
elif wkday == 2:
    shutil.copyfile("/home/pi/mnt/Class_Log/template/WED.html","/home/pi/mnt/Class_Log/" + today + "/main.html")
elif wkday == 3:
    shutil.copyfile("/home/pi/mnt/Class_Log/template/THU.html","/home/pi/mnt/Class_Log/" + today + "/main.html")
elif wkday == 4:
    shutil.copyfile("/home/pi/mnt/Class_Log/template/FRI.html","/home/pi/mnt/Class_Log/" + today + "/main.html")


#index.htmlの読み込み
with open("/home/pi/mnt/Class_Log/index.html", encoding="utf-8") as f:
    html = BeautifulSoup(f.read(),'html.parser')

#動画ページへのリンクの作成
href = "./" + today + "/main.html"
a_tag = Tag(name='a', attrs={
    'class':'contents',
    'href':href,
})
a_tag.string = datetime.datetime.today().strftime("%Y/%m/%d[%a]")
html.find('div', attrs={'class':'main'}).insert(0,a_tag)

print(html.prettify())

#hrefの書き直しあああああああああああああああああああああああああああああああああああああああああああああ
href = "../" + today + "/main.html"
a_tag = Tag(name='a', attrs={
    'class':'contents',
    'href':href,
})
a_tag.string = datetime.datetime.today().strftime("%Y/%m/%d[%a]")


#index.htmlへの上書き
with open("/home/pi/mnt/Class_Log/index.html", mode="w", encoding="utf-8") as f:
    f.write(html.prettify())

if wkday == 0: #月曜日
    #数学へのリンクの追記
    with open("/home/pi/mnt/Class_Log/Tags/sugaku.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("./Tags/sugaku.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

    #国語へのリンクの追記
    with open("/home/pi/mnt/Class_Log/Tags/kokugo.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/kokugo.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

if wkday == 1: #火曜日
    #倫理
    with open("/home/pi/mnt/Class_Log/Tags/rinri.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/rinri.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

    #物理
    with open("/home/pi/mnt/Class_Log/Tags/buturi.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/buturi.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

if wkday == 2: #水曜日
    #数学
    with open("/home/pi/mnt/Class_Log/Tags/sugaku.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/sugaku.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

    #文章
    with open("/home/pi/mnt/Class_Log/Tags/bunsyo.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/bunsyo.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

if wkday == 3: #木曜日
    #化学
    with open("/home/pi/mnt/Class_Log/Tags/kagaku.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/kagaku.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

    #Grammar & Writing
    with open("/home/pi/mnt/Class_Log/Tags/gw.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/gw.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())

if wkday == 4: #金曜日
    #数学
    with open("/home/pi/mnt/Class_Log/Tags/sugaku.html", encoding="utf-8") as f:
        html = BeautifulSoup(f.read(),'html.parser')
    html.find('div', attrs={'class':'main'}).insert(0,a_tag)
    with open("/home/pi/mnt/Class_Log/Tags/sugaku.html", mode="w", encoding="utf-8") as f:
        f.write(html.prettify())





    



    


