#!/usr/bin/env python3
import hmac, hashlib
import os
import math
import time


hash_len = 32
length = 32
key_initial = os.urandom(32)
statekey_initial = os.urandom(32)
salt_key =os.urandom(32)
salt_statekey = os.urandom(32)
S=[]
R=[]
ExpSet = set()

def hmac_sha256(key, data):
    return hmac.new(bytes(key), bytes(data), hashlib.sha256).hexdigest()


def hkdf(length, ikm, salt):
    prk = hmac_sha256(ikm, salt)
    t = b""
    okm = b""
    for i in range(int(math.ceil(length / hash_len))):
        t = hmac_sha256(prk, t + bytes([1+i]))
        okm+=t
    #print{okm}
    return okm[:length]


def hextodecimal(hex):
    return int(hex,16)


def CF(key, index):
    if hextodecimal(hmac_sha256(key,index))<pow(2,242):
        #print(hextodecimal(hmac_sha256(key,index)))
        #print(pow(2, 242))
        return 1
    else:
        #print(hextodecimal(hmac_sha256(key, index)))
        #(pow(2, 242))
        return 0

def checkIndex(n):
    for i in xrange(0,n):
        if i != R[i][0] and i not in ExpSet:
            return 0
        else:
            return 1



def log():
    start_time = time.time()
    statekey = statekey_initial
    key = key_initial
    i=0
    ctr = 0
    with open("loggingevents.txt", "rb") as ins:
        for line in ins:
            key = hkdf(length, key, salt_key)
            #print (key)
            if CF(statekey,bytes(i))==1:
                statekey=hkdf(length,statekey,salt_statekey)
                #print(statekey)
                ctr+=1
                tag=hmac_sha256(statekey,line)
            else:
                tag=hmac_sha256(key,line)
            S.append([line,tag])
            #print(S[i])
            i+=1

    print (ctr)
    with open('loggingresult.txt', 'w') as f:
        for item in S:
            f.write("%s\n" % item)
    print ("%s seconds to log " % (time.time() - start_time))

def recover(n,cs):
    start_time = time.time()
    KS=[]
    SKS=[]
    statekey_r = statekey_initial

    key_r = key_initial

    for i in xrange(0,n+cs):
        key_r = hkdf(length,key_r,salt_key)
        if CF(statekey_r,bytes(i))==1:
            statekey_r=hkdf(length,statekey_r,salt_statekey)
            KS.append([i, statekey_r])
            SKS.append(statekey_r)
        else:
            KS.append([i, key_r])
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

    with open('STATEKEY_R.txt', 'w') as f:
        for item in SKS:
            f.write("%s\n" % item)
    #print(statekey_r)
    if statekey_r is None:
        print("verification fails")
        print("1")
    elif statekey_r != SKS[len(SKS)-1] and statekey_r != SKS[len(SKS)-2]:
        print("verification fails")
        print("2")
    elif len(R)<1:
        print("verification fails")
        print("3")
    elif checkIndex(len(S))==0:
        print("verification fails")
        print("4")
    else:
        with open('recover.txt', 'w') as f:
             for item in R:
                 f.write("%s\n" % item)
    print ("%s seconds to recover " % (time.time() - start_time))





def main():
    log()
    recover(len(S),15000)

main()
#key = hkdf(length, os.urandom(32), salt_key)
#print(hmac_sha256(b'1234567890',bytes(255)))
#print(hmac_sha256(b'i love yo',bytes(255)))


#key1=hkdf(length, os.urandom(64), salt_key)
#print(key)









#hkdf(32,os.urandom(32),os.urandom(32))

#print(int(hmac_sha256(key_initial, salt_key),16))








