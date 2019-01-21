#!/usr/bin/env python3
#Using GGM as PRF

import hmac, hashlib
import os
import math
import time
from Crypto.Cipher import AES
import random
from base64 import b64encode

#hash_len = 32
#length = 32
key_initial = bytes(os.urandom(16))
statekey_initial = bytes(os.urandom(16))
salt_key =bytes(os.urandom(32))
salt_statekey = bytes(os.urandom(32))


S=[]
R=[]
ExpSet = set()
KS = []
SKS = []


def hmac_sha256(key, data):
    return hmac.new(bytes(key), bytes(data), hashlib.sha256).hexdigest()

def hash(key, index):
    return hashlib.sha256(bytes(key)+bytes(index)).hexdigest()





def aes_ctr(key,data):
    cipher = AES.new(key, AES.MODE_CTR)

    nonce = cipher.nonce
    encrypted = cipher.encrypt(data)


    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    #return encrypted
    plaintext = cipher.decrypt(encrypted)
    #
    #
    #print(b64encode(cipher.nonce))
    #print(b64encode(encrypted))
    #print(len(encrypted))
    #print(b64encode(plaintext))
    #print(len(plaintext))
    #print(b64encode(chi))

    #print("The end of one iteration")
    #
    return encrypted


#aes_ctr(key_initial,chi)
#GGF(3)
#print(random.choice([True,False]))


#print(len(data))
#print(b64encode(data))
def hextodecimal(hex):
    return int(hex,16)


def CF(key, index):
    if hextodecimal(hash(key,index))<pow(2,242):
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
    key=key_initial
    #key = key_initial
    i=0
    ctr = 0
    with open("loggingevents_AES.txt", "rb") as ins:
        for line in ins:
            key = aes_ctr(key,salt_key)
            #print (key)
            if CF(statekey,bytes(i))==1:
                statekey=aes_ctr(statekey,salt_statekey)
                #print(statekey)
                ctr+=1
                tag=hmac_sha256(b64encode(statekey),line)
                KS.append([i, b64encode(statekey)])
                SKS.append(b64encode(statekey))
            else:
                tag=hmac_sha256(b64encode(key),line)
                KS.append([i, b64encode(key)])
            S.append([line,tag])
            #print(S[i])
            #i+=1

    #print (ctr)
    with open('loggingresult_AES.txt', 'w') as f:
        for item in S:
            f.write("%s\n" % item)
    print ("%s seconds to log " % (time.time() - start_time))
    return statekey

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


def main():
    statekey_r=log()
    recover(len(S),15000,statekey_r)

main()
#key = hkdf(length, os.urandom(32), salt_key)
#print(hmac_sha256(b'1234567890',bytes(255)))
#print(hmac_sha256(b'i love yo',bytes(255)))


#key1=hkdf(length, os.urandom(64), salt_key)
#print(key)



