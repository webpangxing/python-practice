from  urllib.request import urlopen
from bs4 import BeautifulSoup
import  re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")
images = bsObj.find_all("img",{"src":re.compile("..\/img\/gifts/img.*\.jpg")})

for image in images:
    print(image["src"])
    #tag.attrs 返回爬取标签对象的所有属性
    #Lambda表达式 匿名函数，将函数作为参数使用
    # soup.find_all(lambda tag: len(tag.attrs) == 2)
    #返回有两个属性的标签
