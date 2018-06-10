# -*- coding:utf-8 -*-  
'''
Created on 2018年6月7日

@author: Administrator
'''
from bs4 import BeautifulSoup
with open('test_html.txt',"r") as r_f:
    soup = BeautifulSoup(r_f,"lxml")
    _nav = soup.find("main")#, {"aria-label":"Course"})
    print (_nav)
    _p = _nav.find_all("div",class_="menu-item")
    for i in _p:
        print (i.a.href)
#     for i in _p:
#         if(i.a):
#             print (i.a.href)
#         soup2 = BeautifulSoup(i.get_text(),"lxml")
#         div = soup2.find_all("div",class_="menu-item")
#         for j in div:
#             print (j.a.href)