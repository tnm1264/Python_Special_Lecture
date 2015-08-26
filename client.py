#Client 20103323 Kim tae wook
from socket import *
import datetime

HOST = '127.0.0.1'
PORT = 2000
BUFSIZE = 1024
ADDR = (HOST,PORT)
msg = ''

clntSock = socket(AF_INET, SOCK_STREAM)
clntSock.connect(ADDR)

while True:
	time = datetime.datetime.now()
	msgid = str(time)
	msg = input('> ')
	if not msg or (msg == 'quit'): break
	msg += '\n'
	clntSock.send(bytes(msgid+' '+msg,'UTF-8'))
	msg=''

clntSock.close()