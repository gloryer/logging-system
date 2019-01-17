
import socket
import time
import random
import string
import time


UDP_IP = "127.0.0.1"

UDP_PORT = 5005

Events=[]

events_per_packet =5
def eventsGeneration():
  for i in xrange(1048575):
    s = ''.join (random.choice(string.ascii_letters+string.digits) for x in xrange(80))
    Events.append(s)
    #with open('sending.txt', 'a') as f:
      #f.write("%s \n" % s)
    #print(Events[i])
  print(len(Events))

print "UDP target IP:", UDP_IP

print "UDP target port:", UDP_PORT

def main():
  print "UDP target IP:", UDP_IP
  print "UDP target port:", UDP_PORT

  eventsGeneration()

  clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
  #for i in xrange(0,501,20):
  for i in xrange (0,len(Events),5):
    msg=b''
    for j in xrange (i,i+4):
      msg+=Events[j]
      #print(msg)
    clientSock.sendto(msg, (UDP_IP, UDP_PORT))
    time.sleep(0.005)
  print("DONE!")
  clientSock.close()

main()









#print "message:", msg
#clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP

#clientSock.sendto(msg, (UDP_IP, UDP_PORT))
#print (" %s seconds to send all the packets " %(time.time()-start_time))


