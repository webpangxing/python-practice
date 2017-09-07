from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getCode(url):
    try:
        html = urlopen(url)
    #如果是404
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
    #如果服务器不存在，html就是一个None对象，html.read()就会返回AttributeError
    except AttributeError as e:
        print(e)
        return None
    return bsObj

text = getCode("http://www.baidu.com/")

if text == None:
    print("找不到代码")
else:
    print(text)
