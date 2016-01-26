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
from connectsql import *

idarray = ["A36926F60b00000181d9f976","A36926F60b000001807cd8d6","A36926F60b00000180052928","A36926F60b00000181e2bfc5","A36926F60b00000181d91cfd"
           ,"A36926F60b0000018005292f","A36926F60b0000018005292d","A36926F60b0000018005292b","A36926F60b000001801b9b46"
           ,"A36926F60b0000018005292c","A36926F60b0000018005292e","A36926F60b00000181d91d01","A36926F60b00000181e2da6a","A36926F60b00000181e2d450"
           ,"A36926F60b00000180603a93","A36926F60b00000181d91cf7","A36926F60b00000181e2d84b","A36926F60b00000180052925","A36926F60b00000181e2d861","A36926F60b00000180052929"
           ,"A36926F60b00000181e2dc2b","A36926F60b00000181e2d85d","A36926F60b00000180052931","A36926F60b00000180052930","A36926F60b0000018005292a","A36926F60b00000181e2d859"
           ,"A36926F60b00000180052926","A36926F60b00000181d91cf3"]
url = "http://digimuse.nmns.edu.tw"
#[conn, cur] = connectdb()

dir_name = "ipart_img_new"
if not os.path.exists(dir_name):   
    os.makedirs(dir_name)



for tempstr in idarray:
    #res = requests.get("http://digimuse.nmns.edu.tw/da/repos/0/Handlers/DbTreeViewHandler.ashx?domain=az&field=i0&target=ku&filter=&path=false&uid=1446535533830&id=" + tempstr)
    #soup = BeautifulSoup(res.text)
    #print soup
    typeval = idarray.index(tempstr)+4
    url_str = "http://digimuse.nmns.edu.tw/da/repos/0/Handlers/DbTreeViewHandler.ashx?domain=az&field=i0&target=ku&filter=&path=false&uid=1446535533830&id=" + tempstr
    xml_str = urllib.urlopen(url_str).read()
    xmldoc = minidom.parseString(xml_str)
    obs_values = xmldoc.getElementsByTagName('userdata')
    #print url+obs_values[0].firstChild.data
    
    for obs_val in obs_values:
        urlb = url+obs_val.firstChild.data 
        print urlb
        res = requests.get(urlb)
        soup = BeautifulSoup(res.text,"lxml")
        #print soup
        
        for a in soup.select('#titleName'):
            print a.text
#                print '-------------------------------1'
            word = ""
            for items in soup.select('#contenttext'):
                 word = word + items.text.replace("\n", "")
            print word
#                 print '-------------------------------2'
            for item in soup.select('img'):
                fname = url+item['src']
                str2 ='files'
                if fname.find(str2)!=-1:
                     print fname
                     tx= fname.split('/')[-1]
                     data = urllib.urlopen(fname)
                     f = open(dir_name+'/' + str(tx) ,'wb')
                     f.write(data.read())
                     f.close()
                     
            #insertdata(conn,cur,"object",["type", "cname", "cdes"], [typeval, a.text, word])                

#closedb(conn,cur)
        
        
        