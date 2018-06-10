# -*- coding:utf-8 -*-  
'''
Created on 2018年5月29日

@author: Administrator
'''
import requests
from bs4 import BeautifulSoup
login_url="https://www.cqedx.cn/login"   
client=requests.session()  
client.get(login_url)  
csrf_token=client.cookies['csrftoken'] 
headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    'Host':"www.cqedx.cn",
    'Accept-Encoding':'gzip',
    'Referer': "https://www.cqedx.cn/login?next=/dashboard",
    'X-Requested-With': "XMLHttpRequest",
    'X-CSRFToken':csrf_token
}   
# print headers/
url ='https://www.cqedx.cn/user_api/v1/account/login_session/' #'http://httpbin.org/cookies'
_param ={"email":'edx006@ruitong.cn',"password":'P@ssw0rd','remember':'true'}
r = client.post(url, data=_param,headers = headers)
print (r)
_new_url = 'https://www.cqedx.cn/courses/course-v1:EDX+DAT236x+2018/courseware/0cd24d399d3b45a49c12b59d222518de/eb2c28f63bde496685005ac814d63de8/'
r = client.get(_new_url)  
soup = BeautifulSoup(r.text, "lxml")
_nav = soup.find("nav", {"aria-label":"Course"})
print _nav