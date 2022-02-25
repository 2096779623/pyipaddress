import urllib.request
from bs4 import BeautifulSoup
print("IP: " + BeautifulSoup(urllib.request.urlopen(r'https://ipaddress.com/website/' + input("请输入要获取的网站IP：")).read().decode('utf-8'), 'html.parser').li.text)
