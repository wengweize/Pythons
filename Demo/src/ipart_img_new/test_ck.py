# coding=UTF-8
'''
Created on 2015/12/23

@author: viplab
'''

import requests
from bs4 import BeautifulSoup
from operator import itemgetter
from pip._vendor.requests.packages.urllib3.util.connection import select
from jsonschema._validators import items
import shutil
from xml.dom import minidom
import urllib
import xml.etree.ElementTree as ET
import os
from urllib import urlretrieve
from bs4.builder._lxml import LXML
# from connectsql import *
import re

import requests
from bs4 import BeautifulSoup
from zmq.backend.cython.constants import NULL





res = requests.get("http://gaga.biodiv.tw/new23/9411/148.htm")
soup = BeautifulSoup(res.content,'html.parser')
x=0
ename =""
d=[]
for item in soup.select('b'):
    x=x+1
    d.append(item.text)
Fname=re.sub(r'[\n\s]', '', d[0])
Ename=Fname
print '第一:',Fname

for itemss in soup.select('b'):
#     print itemss.text
    ename = ename + itemss.text.replace("\n","")  
print '第二:',re.sub(r'[\n\s]', '', ename)


g=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','o','w','u','v','x','y','z'
  ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','O','W','U','V','X','Y','Z']

for z in g:
#     print z
    Fname = Fname.replace(z, '')
    #print Fname
print Fname
Ename= Ename.replace(Fname,'')
print Ename
# print 







