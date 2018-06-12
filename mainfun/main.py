#-*- coding:utf-8 -*-  
'''
Created on 2018年6月11日

@author: Administrator
'''
from mainfun.GetClient import get_client
from tools.AnalyseMain import get_result_list
from tools.GetVideoUrl import get_video_url
import random
import time
import requests
import os
from tools.GetSrt import get_srt
def be_relax():
    _first = random.randint(0,1)
    _seconds = random.randint(0,3+_first)
    print ("sleep for little time : "+str(_seconds))
    time.sleep(_seconds)
def get_file_list_as_file():
    with open("data.txt","w+") as save_f:
        _client = get_client()
        if _client!=None:
            _main_page_url = 'https://www.cqedx.cn/courses/course-v1:EDX+DAT236x+2018/courseware/0cd24d399d3b45a49c12b59d222518de/eb2c28f63bde496685005ac814d63de8/'
            _main_page = _client.get(_main_page_url).text
            _lesson_list = get_result_list(_main_page)
            for _lesson in _lesson_list:
                _chapter = _lesson['chapter']
                print ("in chapter named \""+_chapter+'"')
                _item =_lesson["submenu"]
                for i in _item:
                    _subtitle = i['subtitle']
                    print ("in subtitle named \""+_subtitle+'"')
                    _suburl = i['suburl']
                    be_relax()
                    _single_page = _client.get(_suburl).text
                    _sub_lesson = get_video_url(_single_page)
                    for item in _sub_lesson:                  
                        item['title']=_chapter+"#"+_subtitle+"#"+item['title']
                        if item['url']!="":
                            save_f.write(str(item)+'\n')
                        else:
                            print (item['title'],item['url'],item['translation'])
def download(max_num=3):
    _base_save_path = "../download/"
#     _client ="ZXC"
    _client = get_client()
    with open("data.txt","r") as r_f:
        for i in r_f.readlines():
            max_num = max_num - 1
            if max_num < 0:
                break
            print (max_num)
            _dict = eval(i)
#             print (_dict['title'])
#             print (_dict['url'])
#             print (_dict['translation']) 
            if _client!=None:
                _paths = _dict['title'].replace(" | ",".").split('#')
                url_file = _dict['url']
                _srt_url = _dict['translation']
                _save_path=_base_save_path+"/".join(_paths)
                _save_path_file=_base_save_path+"/".join(_paths)+"/"+url_file.split('/')[-1]
                if(os.path.exists(_save_path)):
                    download_video(_client,url_file,_save_path_file)
                    download_srt(_client,_srt_url,_save_path_file)
                    print (_save_path)
                else:
                    os.makedirs(_save_path)
    print("Download Over!!")
#                 
def download_video(_client,url_file,_save_path_file):
    try:
        if os.path.exists(_save_path_file):
            print ("already exit : "+_save_path_file.split('/')[-2])
            return
        be_relax()                    
        r = _client.get(url_file, stream=True)
        f = open(_save_path_file, "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
        f.close()
        print ("download video success! "+_save_path_file.split('/')[-2])
    except:
        print ("download video failed! "+_save_path_file.split('/')[-2])
def download_srt(_client,srt_url,_save_path_file):
    try:
        _real_path =_save_path_file.replace("mp4", "srt")
        if os.path.exists(_real_path):
            print ("already exit : "+_save_path_file.split('/')[-2])
            return
        be_relax()
        r = _client.get(srt_url)
        get_srt(r.text,_path=_real_path)
        print ("download subtitle success! "+_save_path_file.split('/')[-2])
    except:
        print ("download subtitle failed! "+_save_path_file.split('/')[-2])
if __name__ == '__main__':
#     get_file_list_as_file()
    download(1000)
#     _client = get_client()
#     url_file ='https://edxmediastroage.blob.core.chinacloudapi.cn/course/MSXDLEXX2017-V003000_DTH.mp4'
#     _save_path_file = "../download/Welcome to course/Welcome/Welcome/MSXDLEXX2017-V003000_DTH.mp4"
#     srt_url ='https://www.cqedx.cn/courses/course-v1:EDX+DAT236x+2018/xblock/block-v1:EDX+DAT236x+2018+type@video+block@3606d35891bf444a96e9becab340ed64/handler/transcript/translation/en'
#     download_srt(_client,srt_url,_save_path_file)
#     r = _client.get(srt_url)
#     get_srt(r.text,_path=_save_path_file.replace("mp4", "srt"))

        
                    
