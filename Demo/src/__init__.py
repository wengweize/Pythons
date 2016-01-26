#coding=utf-8
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

# idarray = ["A36926F60b00000181d9f976","A36926F60b000001807cd8d6","A36926F60b00000180052928","A36926F60b00000181e2bfc5","A36926F60b00000181d91cfd"
#            ,"A36926F60b0000018005292f","A36926F60b0000018005292d","A36926F60b0000018005292b","A36926F60b000001801b9b46"
#            ,"A36926F60b0000018005292c","A36926F60b0000018005292e","A36926F60b00000181d91d01","A36926F60b00000181e2da6a","A36926F60b00000181e2d450"
#            ,"A36926F60b00000180603a93","A36926F60b00000181d91cf7","A36926F60b00000181e2d84b","A36926F60b00000180052925","A36926F60b00000181e2d861","A36926F60b00000180052929"
#            ,"A36926F60b00000181e2dc2b","A36926F60b00000181e2d85d","A36926F60b00000180052931","A36926F60b00000180052930","A36926F60b0000018005292a","A36926F60b00000181e2d859"
#            ,"A36926F60b00000180052926","A36926F60b00000181d91cf3"]
url = "http://digimuse.nmns.edu.tw"
[conn, cur] = connectdb()

dir_name = "ipart_img_new"
if not os.path.exists(dir_name):   
    os.makedirs(dir_name)
# uids = 1;
 


url_str = "http://digimuse.nmns.edu.tw/da/repos/0/Handlers/DbTreeViewHandler.ashx?domain=az&field=i0&target=ku&filter=&path=false&uid=1446535533830&id=78547F3C0b00000180052924"
xml_str = urllib.urlopen(url_str).read()
xmldoc = minidom.parseString(xml_str)
obs_v = xmldoc.getElementsByTagName('item')

# print obs_v[0].getAttribute("name")

for t in obs_v:
# try:
    classid = t.getAttribute("id")
    classtext = t.getAttribute("text")
    ctexts=classtext.split(' ')
    query = "select insertclass(1,'"+ctexts[0]+"');"
    
#     print query 
    insertquery(conn,cur,query)
    maxcid=select_onedata(cur,"class","max(cid)")
    cid = maxcid[0]
    print "insert class "+str(cid)+"  "+ctexts[0]+"\n"
#     cur.execute("INSERT INTO " + table + " (" + tempstr + ") VALUES (" + tempdata + ");", data)
    
#   insert class(classtext)  return cid

    url_str = "http://digimuse.nmns.edu.tw/da/repos/0/Handlers/DbTreeViewHandler.ashx?domain=az&field=i0&target=ku&filter=&path=false&uid=1446535533830&id="+ classid
    xml_str = urllib.urlopen(url_str).read()
    xmldoc = minidom.parseString(xml_str)
    obs_values = xmldoc.getElementsByTagName('userdata')
    #print url+obs_values[0].firstChild.data
     
    for obs_val in obs_values:
#     try:
        urlb = url+obs_val.firstChild.data 
#         print urlb
        query = "select inserturl('"+urlb+"');"
        insertquery(conn,cur,query)
        maxoid=select_onedata(cur,"object","max(oid)")
        oid = maxoid[0]
        print "insert url "+str(oid)+"  "+urlb+"\n"
        
        res = requests.get(urlb)
        soup = BeautifulSoup(res.text,"lxml")
        #print soup
         
        for a in soup.select('#titleName'):
#         try:
            #print a.text
#                print '-------------------------------1'
            ccname = ""
            try:
                ccname = ccname+a.text.replace(u"Guen'ee,", " ")
            except:
                ccname = ""
            word = ""
            for items in soup.select('#contenttext'):
                try:
                    word = word + items.text.replace("\n", "")
                    word = word.replace(u"é", " ")
                    word = word.replace(u"Guen'ee,", " ")
                except:
                    word = ""
            #print word
#                 print '-------------------------------2'
            #i = 0
            fnames = []
            for item in soup.select('img'):
                fname = url+item['src']
                str2 ='files'
                if fname.find(str2)!=-1:
                   fnames.append(fname)
                   print fname
                   #insertquery(conn,cur,query)
                   #urlimage=select_onedata(cur,"object","sourceurl")
#                      tx= fname.split('/')[-1]
#                      data = urllib.urlopen(fname)
#                      f = open(dir_name+'/' + str(tx) ,'wb')
#                      f.write(data.read())
#                      f.close()
            if fnames:
                query = "update object set cname = '"+ccname+"' ,cdes = '"+word+"',sourceurl = '"+fnames[0]+"' where oid = "+str(oid)+";"    
            else:
                query = "update object set cname = '"+ccname+"' ,cdes = '"+word+"' where oid = "+str(oid)+";"
            print query
            try:
                insertquery(conn,cur,query)
#             print "update obj "+str(oid)+"  "+a.text+"  "+word+"\n"
                insertdata(conn, cur,"co",["cid","oid"],[cid,oid])
                print "co "+str(cid)+"  "+str(oid)+"\n"
            except:
                closedb(conn,cur)
                [conn, cur] = connectdb()
                
                            
            #insertdata(conn,cur,"object",["type","cname","cdes"], [typeval,a,word])         
#             insertdata(conn, cur,"url",["uid","hostname"],[uids,urlb])

#         except:
#             print "insert obj err\n"
#             continue #insert obj err
#     except:
#         print "insert url err\n"
#         continue # insert url err
# except:
#     print "insert class error\n"
#     continue #insert class error
        
        
closedb(conn,cur)
