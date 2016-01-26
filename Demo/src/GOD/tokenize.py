# coding=UTF-8
import psycopg2

conn_host='127.0.0.1'
conn_database='moth_dbGOD'
conn_user='postgres'
conn_password='viplab4719'
dbdata = 'host=' + conn_host + ' dbname=' + conn_database + ' user=' + conn_user + ' password=' + conn_password

conn = psycopg2.connect(dbdata)
cur = conn.cursor()

cur.execute("select oid from vd_dc_des where databyte is null")

pidarray = []

for pid in cur:
	pidarray.append(pid[0])

for pid in pidarray:
	print pid
	cur.execute("select Tokenize(%s,%s)", (pid, 3))
	conn.commit()

cur.execute("select tid, words from Token")

tidarray = []
wordarray = []

for tid in cur:
	tidarray.append(tid[0])
	wordarray.append(tid[1])

for tid in xrange(len(tidarray)):
	try:
		cur.execute("select CountSE(%s,%s)", (tidarray[tid], wordarray[tid]))
		conn.commit()
	except Exception, e:
		print 'Error'
		cur.close()   
		conn.close()
		conn = psycopg2.connect(dbdata)
		cur = conn.cursor()

cur.close()   
conn.close()