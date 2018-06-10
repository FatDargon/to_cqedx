# -*- coding:utf-8 -*-  
import sys  
import requests  
import time  
import string  
  
login_url="https://www.cqedx.cn/login"  
login_params={'email':'12345678@mooc.buaa.edu.cn','password':'12345678'}  
client=requests.session()  
client.get(login_url)  
csrf_token=client.cookies['csrftoken'] 
