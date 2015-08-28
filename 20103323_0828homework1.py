#20103323 김태욱 Day05(0828) - homework1 : 시간이름을 가진 데이터를 적절히 파싱하여 DB에 넣기
import time
import datetime
import random
import sqlite3

#file들의 list를 만든다.
fileList = []

#시간과 랜덤데이터가 기록된 파일 10개 생성
cur = datetime.datetime.now()
dt = datetime.timedelta(minutes=1)
count = 0
today = cur.strftime('%Y%m%d')+'_DATA'
fileList.append(today)
print('Today is '+today)
while True:
	if count>0:break #파일이 여러개일 경우 시간이 너무 오래걸려서 2개의 파일만 생성하도록 설정
	cur=cur+dt
	filename = cur.strftime('%Y%m%d_DATA')
	if(filename!=today):
		#print(filename[:-5])
		fileList.append(filename)
		today = filename
		count+=1
	data_time = cur.strftime('%Y%m%d%H%M')
	d1 = random.randrange(0,9999)
	d2 = random.randrange(0,9999)
	d3 = random.randrange(0,9999)
	data = '{0},{1:4d},{2:4d},{3:4d}\n'.format(data_time,d1,d2,d3)
	with open(filename,'a') as f:
		f.write(data)

#DB파일을 만들고 DB에 넣기
con = sqlite3.connect('TimeAndRandomData.db')
cur = con.cursor()
#이미 존재하는 table일 것을 대비한 try, except, finally 문
try:
	cur.execute("CREATE TABLE TimeAndRandomDataTable(Year text, Month text, Day text, Hour text, Minute text, Data1 text, Data2 text, Data3 text);")
	for name in fileList:
		with open(name,'r') as f:
			while True:
				line = f.readline()
				if not line: break
				token = line.split(',')
				year = int((token[0])[:4])
				month = int((token[0])[4:6])
				day = int((token[0])[6:8])
				hour = int((token[0])[8:10])
				minutes = int((token[0])[10:12])
				data1 = int(token[1])
				data2 = int(token[2])
				data3 = int(token[3])
				query = "INSERT INTO TimeAndRandomDataTable VALUES('"+year+"','"+month+"','"+day+"','"+hour+"','"+minutes+"','"+data1+"','"+data2+"','"+data3+"');"
				cur.execute(query)
				con.commit()

except sqlite3.OperationalError:
	for name in fileList:
		with open(name,'r') as f:
			while True:
				line = f.readline()
				if not line: break
				token = line.split(',')
				year = str(int((token[0])[:4]))
				month = str(int((token[0])[4:6]))
				day = str(int((token[0])[6:8]))
				hour = str(int((token[0])[8:10]))
				minutes = str(int((token[0])[10:12]))
				data1 = str(int(token[1]))
				data2 = str(int(token[2]))
				data3 = str(int(token[3]))
				query = "INSERT INTO TimeAndRandomDataTable VALUES('"+year+"','"+month+"','"+day+"','"+hour+"','"+minutes+"','"+data1+"','"+data2+"','"+data3+"');"
				cur.execute(query)
				con.commit()
finally:
	print('complete') #완료 message
	cur.execute("SELECT * FROM TimeAndRandomDataTable;") #DB에 제대로 들어갔는지 확인하기 위한 select문
	print(cur.fetchall())
	cur.close()
	con.close()
	



