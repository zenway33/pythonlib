#打印所有url
import requests
import lxml
from bs4 import BeautifulSoup

headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }

r = requests.get("http://bbs.linuxtone.org", headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
#soup = BeautifulSoup(r.text, "lxml")

print(soup.title.text)
#print(soup.body.text)

for x in soup.findAll("a"):
    print(x['href'])

#打印所有图片
tags=soup.findAll('img')
print("\n".join(set(tag['src'] for tag in tags)))





