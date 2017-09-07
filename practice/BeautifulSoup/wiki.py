from urllib.request import urlopen
from  bs4 import BeautifulSoup
import  re
import datetime
import random

random.seed(datetime.datetime.now())#seed函数没有返回值,改变随机生成器的种子
file = open('wiki.txt','a+')

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bs_obj = BeautifulSoup(html,"html.parser")
    return bs_obj.find("div",{"id":"bodyContent"}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
num = 0
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    file.write(newArticle+'\n')
    links = getLinks(newArticle)
    num+=1
    if num >100:
        file.close()
        break
