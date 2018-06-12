# -*- coding:utf-8 -*-
'''
Created on 2018年6月7日

@author: Administrator
'''
from bs4 import BeautifulSoup
from tools.mprint import pretty_list
import re
import json
def get_video_url(str):
    _result = []
    soup = BeautifulSoup(str, "lxml")
    seq_contents = soup.find_all("div",class_=re.compile("seq_contents"))
    for _content in seq_contents:
        _item = {
            "title": "",
            "url": "",
            "translation":""
        }
        _content_text = _content.get_text(strip= True)
        soup2 = BeautifulSoup(_content_text, "lxml")
        _title = soup2.find("h3").get_text()
        _item['title'] = _title
        # print (_title)
        _div = soup2.find_all("div",class_="video closed")
        for i in _div:
            # print (i['data-metadata'])
            soup3 = BeautifulSoup(i['data-metadata'],"lxml")
            for i in soup3.find_all(text= re.compile("mp4")):
                # try:
                ii = json.loads(i)
                _url = ii["sources"][0]
                _item['url']=_url
                _lang = ii["transcriptLanguage"] 
                base_url = 'https://www.cqedx.cn'
                _translation = base_url+ii["transcriptTranslationUrl"].replace("__lang__",_lang)
                _item["translation"]=_translation
        _result.append(_item)
        del _item
    return _result
if __name__ == '__main__':
    with open('../test/test_html.txt',"r") as r_f:
        _result = get_video_url(r_f)
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