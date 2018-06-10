# -*- coding:utf-8 -*-  
'''
Created on 2018年6月7日

@author: Administrator
'''
from bs4 import BeautifulSoup
from tools.mprint import pretty_list
with open('test_html.txt',"r") as r_f:
    _result =[]
    _item = {
        "chapter":"",
        "submenu":[]
    } 
    _subitem ={
        "subtitle":"",
        "suburl":""
    }
    soup = BeautifulSoup(r_f,"lxml")
    _nav = soup.find("nav",class_="course-navigation")#, {"aria-label":"Course"})
#     print (_nav)
    _as =  _nav.find_all("a",class_="button-chapter")
    for _a in _as:
        chapter_name = _a.get_text(strip=True)
        print (chapter_name)
        _item["chapter"] = chapter_name
        j=_a.next
        while(j!=None):
            try:
                _p = j.find_all("a",class_="accordion-nav")
            except:
                _p = []
            if (_p!= []):
                for i in _p:
                    suburl = i.href
                    subtitle = i.get_text(strip=True).replace("current section","")
                    _subitem["subtitle"]=subtitle
                    _subitem["suburl"]=suburl
                    _item["submenu"].append(_subitem)
                    print (suburl)
                    print('^'*20)
                    print (subtitle)
            j=j.next
        _result.append(_item)
    pretty_list (_result)
#     _p = _nav.find_all("a",class_="accordion-nav")
#     for i in _p:
#         print (i)
#         print('^'*20)
#         print (i.p.get_text())
#     for i in _p:
#         if(i.a):
#             print (i.a.href)
#         soup2 = BeautifulSoup(i.get_text(),"lxml")
#         div = soup2.find_all("div",class_="menu-item")
#         for j in div:
#             print (j.a.href)