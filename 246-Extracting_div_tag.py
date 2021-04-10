import requests
from bs4 import BeautifulSoup

r=requests.get("http://century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")  #delete www. 
c=r.content

soup=BeautifulSoup(c,"html.parser")

# use beautiful soup to find the target  tags elements
all=soup.find_all("div",{"class":"infinite-item"})         

# all[0]    可以显示出抓取中的第一个内容的部分。
#type(all)  可以检查出抓去内容的格式。
#len(all)   可以检查出抓取内容的总长度.
#len(all)   可以检测出一共几个内容被抓到。
all[0]      

#find the price, but there are still sth else.
all[0].find_all("a",{"class":"listing-price"})

#find the price ,and next, remove all the characters.
all[0].find("a",{"class":"listing-price"}).text

#替换多余的符号
all[0].find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","") 