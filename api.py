import urllib.request
from bs4 import BeautifulSoup
website = input("请输入要获取的网站IP：")
url = r'https://ipaddress.com/website/' + website
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
ip = soup.li.text
print("IP：" + ip)