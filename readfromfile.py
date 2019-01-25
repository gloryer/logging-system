import time
def readlines():
    num_lines = sum(1 for line in open('loggingevents_AES.txt'))
    print(num_lines)
# import hashlib
# import os
#
# def hash(key, index):
#     return hashlib.sha256(bytes(key)+bytes(index)).hexdigest()
#
#
# print(len(hash(os.urandom(16),0)))


def read():
    S=[]
    start_time = time.time()
    with open("loggingresult_AES.txt", "rb") as ins:
        for line in ins:
            S.append(line)


    with open('storing.txt', 'w') as f:
        for item in S:
            f.write("%s\n" % item)

            #print(S[i])

    print ("%s seconds to read " % (time.time() - start_time))

#readlines()
#readlines()
#readlines()


def read2():
    S=[]
    start_time = time.time()
    with open("loggingevents_AES.txt", "rb") as ins:
        for line in ins:
            #S.append(line)
            with open('storing.txt', 'a') as f:
                 f.write("%s\n" % line)

            #print(S[i])

    print ("%s seconds to read " % (time.time() - start_time))



read2()
