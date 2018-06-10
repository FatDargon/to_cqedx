# -*- coding:utf-8 -*-  
'''
Created on 2018年5月29日

@author: Administrator
'''
import requests
from bs4 import BeautifulSoup
url ='https://www.cqedx.cn/courses/course-v1:EDX+DAT236x+2018/courseware' #'http://httpbin.org/cookies'
cookies = '''
    csrftoken=2i8Em5k19ckqk37Nn5PluKqNyCBCpVWb; edxloggedin=true; sessionid="1|blqzbydkp43a5a0n5tqfb7b433jsr8fh|OCgOvsvsiF0i|ImQ5NTc2MTJjMmM5ZWE2NjYwOTFkMDRjNzQ1YTQwMjM2NTgyMjJiZjY1ZWI4NjZiYzg2NTc0MTU3NDExMDNkOTMi:1fNc8E:H_9ws_uJc1Wwqfb_WatBS0gbl5Y"; edx-user-info="{\"username\": \"edx006\"\054 \"version\": 1\054 \"enrollmentStatusHash\": \"30ec7e5bb592fe5e97b10d95f7fbbd44\"\054 \"header_urls\": {\"learner_profile\": \"https://www.cqedx.cn/u/edx006\"\054 \"logout\": \"https://www.cqedx.cn/logout\"\054 \"account_settings\": \"https://www.cqedx.cn/cookies/settings\"}}"
    '''
cookie_dict = dict((line.split('=') for line in cookies.strip().split(";")))
r = requests.get(url, cookies=cookie_dict)
print r.text
soup = BeautifulSoup(r.text, "lxml")
_nav = soup.find("nav", {"aria-label":"Course"})
print _nav