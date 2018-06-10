# -*- coding:utf-8 -*-  
'''
Created on 2018年6月7日

@author: Administrator
'''
from bs4 import BeautifulSoup
from tools.mprint import pretty_list
def get_result_list(str):
    _result = []

    soup = BeautifulSoup(r_f, "lxml")
    _nav = soup.find("nav", class_="course-navigation")  # , {"aria-label":"Course"})
    #     print (_nav)
    _as = _nav.find_all("a", class_="button-chapter")
    for _a in _as:
        _item = {
            "chapter": "",
            "submenu": []
        }
        chapter_name = _a.get_text(strip=True)
        # print (chapter_name)
        _item["chapter"] = chapter_name
        j = _a.next
        while (True):
            try:
                _p = j.find_all("a", class_="accordion-nav")
            except:
                _p = []
            if (_p != []):
                for i in _p:
                    _subitem = {
                        "subtitle": "",
                        "suburl": ""
                    }
                    base_url = 'https://www.cqedx.cn'
                    suburl = base_url + i['href']
                    subtitle = i.get_text(strip=True).replace("current section", "")
                    _subitem["subtitle"] = subtitle
                    _subitem["suburl"] = suburl[-3:]
                    _item["submenu"].append(_subitem)
                    del _subitem
                    # print (suburl)
                    # print('^'*20)
                    # print (subtitle)
                break
            j = j.next
        _result.append(_item)
        del _item
    return _result
if __name__ == '__main__':
    with open('test_html.txt',"r") as r_f:
        _result = get_result_list(r_f)
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