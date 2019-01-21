import time
def readlines():
    num_lines = sum(1 for line in open('recover_udp.txt'))
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
read()


def recover(n,cs,skey):
    KS2=[]
    start_time = time.time()
    #KS=[]
   # SKS=[]
    #statekey_r = statekey_initial

    # = key_initial
    statekey_r_2= statekey_initial
    key_r=key_initial

    for i in xrange(0,n+cs):
     key_r = aes_ctr(key_r,salt_key)
     if CF(statekey_r_2,bytes(i))==1:
        statekey_r_2=aes_ctr(statekey_r_2,salt_statekey)
        KS2.append([i, b64encode(statekey_r_2)])
        #SKS.append(b64encode(statekey_r))
     else:
         KS2.append([i, b64encode(key_r)])
    #for i in range (0,n):
        #print(KS[i])

    for i in xrange(0, n-cs+1):
        if hmac_sha256(KS[i][1],S[i][0])==S[i][1]:
            R.append([i,S[i][0]])
            #print("good")

    for i in xrange(n-cs+1,n):
        if hmac_sha256(KS[i][1],S[i][0])==S[i][1]:
            R.append([i, S[i][0]])
        else:
            ExpSet.add("i")
    for i in xrange(n,n+cs):
            ExpSet.add("i")
    #if R is None:
        #print ("null")
    #for item in R:
       #print(item )

    with open('STATEKEY_R_AES.txt', 'w') as f:
        for item in SKS:
            f.write("%s\n" % item)
    with open('KS_AES.txt', 'w') as f:
        for item in KS:
            f.write("%s\n" % item)
    #print(statekey_r)
    if b64encode(skey) is None:
        print("verification fails")
        print("1")
    elif b64encode(skey)!= SKS[len(SKS)-1] and b64encode(skey)!= SKS[len(SKS)-2]:
        print("verification fails")
        print("2")
    elif len(R)<1:
        print("verification fails")
        print("3")
    elif checkIndex(len(S))==0:
        print("verification fails")
        print("4")
    else:
        print("Successfully recovery!")
        # with open('recover_AES.txt', 'w') as f:
             #for item in R:
                 #f.write("%s\n" % item)

    print ("%s seconds to recover " % (time.time() - start_time))
