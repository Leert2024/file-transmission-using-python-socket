from socket import *
import os
mysocket = socket(AF_INET,SOCK_STREAM)
IP="192.168.0.102"
PORT=1024
mysocket.connect((IP,PORT))
NAME = "snake_game.rar"
SIZE = os.stat(NAME).st_size
mysocket.send((NAME+" "+str(SIZE)).encode())
print('准备向目标主机 '+IP+' 的 '+str(PORT)+' 端口发送文件 '+NAME+' ,大小为 '+str(SIZE)+'字节.')
print("等待对方同意...")

IF_SEND = int((mysocket.recv(1024)).decode())
print("对方已同意接收文件,正在发送文件...")
if IF_SEND:
	file = open(NAME,mode = "rb")
	read_size = 0
	while read_size<SIZE:
		chunk = file.read(1024)
		mysocket.send(chunk)
		read_size += len(chunk)
	file.close()
	print("发送成功!")
mysocket.close()
print('运行结束,按回车键退出!')
input()
