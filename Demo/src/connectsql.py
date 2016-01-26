# coding=UTF-8
import psycopg2
from settings import *
from nbconvert.exporters.export import export

def connectdb():
	conn = psycopg2.connect(dbdata)
	cur = conn.cursor()
	return [conn,cur]

def insertdata(conn,cur,table,col,data):
	tempstr = ""
	tempdata = ""
	for x in range(len(col)):
		if(x < (len(col)-1)):
			tempstr = tempstr + col[x] + ", "
			tempdata = tempdata + "%s, "
		else:
			tempstr = tempstr + col[x]
			tempdata = tempdata + "%s"
	cur.execute("INSERT INTO " + table + " (" + tempstr + ") VALUES (" + tempdata + ");", data)
	# cur.execute(sql)
	conn.commit()

def select_onecoldata(cur,table,col):
	cur.execute("SELECT " + col + " FROM " + table + ";")
	# cur.execute("SELECT url FROM datasource where dsid < 20;")
	return cur.fetchall()

def select_onedata(cur,table,col):
	cur.execute("SELECT " + col + " FROM " + table + ";")
	# cur.execute("SELECT url FROM datasource where dsid < 20;")
	return cur.fetchone()

def closedb(conn,cur):
	cur.close()   
	conn.close()
	
def insertquery(conn,cur,query):
		cur.execute(query)
		# cur.execute(sql)
		conn.commit()
	
	
