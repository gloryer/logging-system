

import hmac, hashlib
import os
import math
import time
from Crypto.Cipher import AES
import random
from base64 import b64encode
from Crypto.Cipher import ChaCha20



#hash_len = 32
#length = 32
key_initial = bytes(os.urandom(32))
statekey_initial = bytes(os.urandom(32))
chi_S =bytes(os.urandom(32))
chi_SC = bytes(os.urandom(32))
nonce_chacha20=bytes(os.urandom(8))


S=[]
R=[]
ExpSet = set()
KS = []
SKS = []
period=[]


def hmac_sha256(key, data):
    return hmac.new(bytes(key), bytes(data), hashlib.sha256).hexdigest()

def hash(key, index):
    return hashlib.sha256(bytes(key)+bytes(index)).hexdigest()


def chacha20(key,data):
    #print(b64encode(data))
    cipher = ChaCha20.new(key=key,nonce=nonce_chacha20)

    encrypted = cipher.encrypt(data)

    cipher=ChaCha20.new(key=key,nonce=nonce_chacha20)
    #plaintext = cipher.decrypt(encrypted)
    #print(len(encrypted))
    #print(b64encode(encrypted))
    #print(b64encode(plaintext))
    return encrypted
#chacha20(key_initial,chi)


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

def checkIndex(n,R):
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
    with open("loggingevents_chacha.txt", "rb") as ins:
        for line in ins:
            key = chacha20(key,chi_S)
            #print (key)
            if CF(statekey,bytes(i))==1:
                pre_statekey=statekey
                statekey=chacha20(statekey,chi_SC)
                #print(statekey)
                ctr+=1
                tag=hmac_sha256(b64encode(statekey),line+b64encode(pre_statekey))
                KS.append([i, b64encode(statekey),b64encode(pre_statekey)])
                SKS.append(b64encode(statekey))
                period.append(i)
            else:
                tag=hmac_sha256(b64encode(key),line+"null")
                KS.append([i, b64encode(key),"null"])
            S.append([line,tag])
            i+=1

    print (ctr)
    with open('loggingresult_chacha.txt', 'w') as f:
        for item in S:
            f.write("%s\n" % item)
    print ("%s seconds to log " % (time.time() - start_time))
    with open('period6.txt', 'w') as f:
        for item in period:
            f.write("%s\n" % item)

    with open('STATEKEY_R_chacha.txt', 'w') as f:
         for item in SKS:
             f.write("%s\n" % item)
    with open('KS_chacha.txt', 'w') as f:
         for item in KS:
             f.write("%s\n" % item)

    return statekey


def recover(n,cs,skey):
    KS2=[]
    SKS2=[]
    start_time = time.time()
    j=0
    K= set ()
    #KS=[]
   # SKS=[]
    #statekey_r = statekey_initial

    key_r = key_initial
    statekey_r_2= statekey_initial

    for i in xrange(0,n+cs):
         key_r = chacha20(key_r,chi_S)
         if i == n + 1:
             K.add(b64encode(statekey_r_2))
         if CF(statekey_r_2,bytes(i))==1:
            pre_statekey_r_2=statekey_r_2
            statekey_r_2=chacha20(statekey_r_2,chi_SC)
            KS2.append([i, b64encode(statekey_r_2),b64encode(pre_statekey_r_2)])
            SKS2.append(b64encode(statekey_r_2))
         else:
            KS2.append([i, b64encode(key_r),"null"])

    K.add(b64encode(statekey_r_2))
    print(K)

    with open("loggingevents_chacha.txt", "rb") as ins:
         for line in ins:
             if hmac_sha256(KS2[j][1],line+KS2[j][2])==S[j][1]:
                   R.append([j,line])
             j+=1


    for i in xrange(n - cs + 1, n+cs):
        ExpSet.add(i)

    if b64encode(skey) is None:
        print("verification fails")
        print("1")
    elif b64encode(skey) not in K:
        print("verification fails")
        print("2")
    elif b64encode(skey)!= SKS[len(SKS)-1] and b64encode(skey)!= SKS[len(SKS)-2]:
        print("verification fails")
        print("3")
    elif len(R)<1:
        print("verification fails")
        print("4")
    elif checkIndex(len(S),R)==0:
        print("verification fails")
        print("5")
    else:
        print("Successfully recovery!")

    with open('recover_chacha20.txt', 'w') as f:
        for item in R:
            f.write("%s\n" % item)

    print ("%s seconds to recover " % (time.time() - start_time))





def main():
    statekey_r=log()
    print(b64encode(statekey_r))

    recover(len(S),1500,statekey_r)

main()

#key = hkdf(length, os.urandom(32), salt_key)
#print(hmac_sha256(b'1234567890',bytes(255)))
#print(hmac_sha256(b'i love yo',bytes(255)))


#key1=hkdf(length, os.urandom(64), salt_key)
#print(key)



