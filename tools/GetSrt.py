# -*- coding:utf-8 -*-  
'''
Created on 2018年6月7日

@author: Administrator
'''
import json
def int2srttime(st):
    _msec = st % 1000
    st = st//1000
    _sec = st % 60
    st = st//60
    _min = st %60
    st = st//60
    _hour = st 
    return "{:0>2d}:{:0>2d}:{:0>2d},{:0>3d}".format(_hour,_min,_sec,_msec)
def get_srt(load_f,_path=""):
    with open(_path,"w",encoding = "utf-8") as w_f:
        load_dict = eval(load_f)
        _start = load_dict['start']
        _end =  load_dict['end']
        _content  = load_dict["text"]
        for i in range(len(_start)):
            w_f.write(str(i+1)+'\n') 
            w_f.write(int2srttime(_start[i])+" --> "+int2srttime(_end[i])+'\n')
            w_f.write( _content[i]+'\n\n')
if __name__ == '__main__': 
    with open("../test/1.txt","r") as load_f:
        get_srt(load_f,"../mainfun/demo.srt")
    
