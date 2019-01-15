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



def hmac_sha256(key, data):
    return hmac.new(b'key', data, hashlib.sha256).hexdigest()


def hkdf(length, ikm, salt):
    prk = hmac_sha256(ikm, salt)
    t = b""
    okm = b""
    for i in range(int(math.ceil(length / hash_len))):
        t = hmac_sha256(prk, t + bytes([1+i]))
        okm+=t
    #print{okm}    return okm[:length]


def hextodecimal(hex):
    return int(hex,16)


def CF(key, index):
    if hextodecimal(hmac_sha256(key,index))<pow(2, 242):
        #print(hextodecimal(hmac_sha256(key,index)))
        #print(pow(2, 242))
        return 1
    else:
        #print(hextodecimal(hmac_sha256(key, index)))
        #(pow(2, 242))
        return 0




def log():
    start_time = time.time()
    statekey = statekey_initial
    key = key_initial
    i=0
    S=[]
    ctr = 0
    with open("loggingevents.txt", "rb") as ins:
        for line in ins:
            key = hkdf(length, key, salt_key)
            #print (statekey)
            if CF(statekey,bytes(i))==1:
                statekey=hkdf(length,statekey,salt_statekey)
                ctr+=1
                tag=hmac_sha256(statekey,line)
            else:
                tag=hmac_sha256(key,line)
            S.append([line,tag])
            #print(S[i])
            i+=1
    print (" %s seconds to generate all system events " % (time.time() - start_time))
    print (ctr)

def recover(n,cs):
    R=[]
    ExpSet=[]
    KS=[]
    statekey_r =  statekey_initial
    key_r = key_initial

    for i in xrange(0,n+cs):
        key_r = hkdf(length,key_r,salt_key)
        KS.append([i,key_r])


def main():
    log()

main()






#hkdf(32,os.urandom(32),os.urandom(32))

#print(int(hmac_sha256(key_initial, salt_key),16))








