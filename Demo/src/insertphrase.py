# coding=UTF-8
import psycopg2

conn_host='127.0.0.1'
conn_database='moth_dbGOD'
conn_user='postgres'
conn_password='viplab4719'
dbdata = 'host=' + conn_host + ' dbname=' + conn_database + ' user=' + conn_user + ' password=' + conn_password

conn = psycopg2.connect(dbdata)
cur = conn.cursor()

cur.execute("select words from Token where phrase = true")

wordarray = []

for word in cur:
	wordarray.append(word[0])

for word in wordarray:
	cur.execute("insert into Phrase(words,type) values(%s,%s)", (word,1))
	conn.commit()
	print 'Insert: ' + word + ' OK!'

cur.close()   
conn.close()