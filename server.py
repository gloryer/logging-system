
import socket
import time



UDP_IP = "127.0.0.1"

UDP_PORT = 5005
data_buffer=[]
serversock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP

serversock.bind((UDP_IP, UDP_PORT))


#timeout = time.time() + 3600
while True:
#for i in range(0.1):
    # if time.time() > timeout:
        #break
     data, addr = serversock.recvfrom(168820736)  # buffer size is 1024 bytes
     with open('receiving20.txt', 'a') as f:
         f.write("%s \n"%data)



#serversock.close()



