from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

bsObj = BeautifulSoup(html)

nameList = bsObj.find_all("span",{"class":"green"})

for name in nameList:
    print(name.get_text())
    #get_text()会把标签清除，返回字符串