import random
import string
import time

def eventsGeneration():
  wr = open('loggingevents.txt','w')
  start_time = time.time()
  for i in xrange(2**20):
    s = ''.join (random.choice(string.ascii_letters+string.digits) for x in xrange(160))
    wr.write(s + "\n")
  print (" %s seconds to generate all system events " %(time.time()-start_time))
  wr.close()


eventsGeneration()