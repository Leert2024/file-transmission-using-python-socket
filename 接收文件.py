#引入socket库
from socket import *

#创建套接字，AF_INET表示网络层使用IP协议，SOCK_STREAM表示传输层使用TCP协议
mysocket = socket(AF_INET,SOCK_STREAM)

#绑定地址与端口
IP = gethostbyname(gethostname())
for i in range(1024,49152):
    try:
        mysocket.bind((IP,i))
        print("成功将socket绑定至"+IP+"的"+str(i)+"端口。")
        break
    except OSError:
        continue
    
#开始监听（阻塞直至接收到连接）
mysocket.listen(1)
print("正在等待客户端连接……")

#接受一个客户端连接
conn, addr = mysocket.accept()
print("接受了一个客户端连接,地址为：",addr)

#获取文件名与文件大小
NAME_AND_SIZE = ((conn.recv(1024)).decode()).split(" ")
NAME = NAME_AND_SIZE[0]
SIZE = int(NAME_AND_SIZE[1])
print("接收的文件名为："+NAME)
print("即将接收的文件大小为："+str(SIZE)+"字节")
print("是否接收？")
IF_RECV = int(input("（输入1开始接收，输入0退出）"))
if IF_RECV:
    #告知对方已做好接收文件的准备
    conn.send("1".encode())

    #打开文件
    file = open(NAME,mode = "wb")
    
    #开始接收文件
    print("开始接受文件……")
    accept_size = 0
    while accept_size<SIZE:
        data = conn.recv(1024)#recv阻塞当前进程，直至接收到信息
        file.write(data)
        file.flush()
        accept_size += len(data)
    file.close()
    print("文件 "+NAME+" 接收成功！")

#关闭连接
mysocket.close()
conn.close()
print("运行结束，按Enter退出！")
input()
    

