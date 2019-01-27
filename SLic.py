

import hmac, hashlib
import os
import time
import random
from base64 import b64encode
from Crypto.Cipher import ChaCha20
import string
from Crypto.Cipher import AES



key_initial = bytes(os.urandom(32))
statekey_initial = bytes(os.urandom(32))
chi_S =bytes(os.urandom(32))
chi_SC = bytes(os.urandom(32))
lam = pow(2,15)
nonce_chacha20=bytes(os.urandom(8))


S=[]
R=[]
ExpSet = set()
KS = []
SKS = []

def Gen_Dummy():
    start_time=time.time()
    key=key_initial
    for i in xrange(2**15):
        s = ''.join(random.choice(string.ascii_letters + string.digits) for x in xrange(160))
        S.append(s)
            # with open('sending.txt', 'a') as f:
            # f.write("%s \n" % s)
            # print(Events[i])
    for i in range(0,len(S)):
        key=chacha20(key,chi_S)
        ct=aes_ctr(key,S[i])
        tag = hmac_sha256(b64encode(key), ct)
        S[i]=[b64encode(ct),tag,b64encode(key)]


    with open('Slic_Gen.txt', 'w') as f:
        for item in S:
            f.write("%s\n" % item)

    print ("%s seconds to log " % (time.time() - start_time))


def SLic_Log():
    start_time = time.time()
    key = key_initial
    i=0
    with open("loggingevents_chacha5.txt", "rb") as ins:
        for line in ins:
            key = chacha20(key,chi_S)

            ct = aes_ctr(key, line)
            tag = hmac_sha256(b64encode(key), ct)
            element= [b64encode(ct), tag, b64encode(key)]

            pos=random.randint(1,lam+i)

            if pos==lam+i:
               S.append(element)
            else:
               swap=S[pos]
               S[pos]=element
               S.append(swap)
            i+=1

    with open('loggingresult_SLic.txt', 'w') as f:
        for item in S:
            f.write("%s\n" % item)
    print ("%s seconds to log " % (time.time() - start_time))







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

    return encrypted

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


def main():
    Gen_Dummy()
    SLic_Log()

main()

#key = hkdf(length, os.urandom(32), salt_key)
#print(hmac_sha256(b'1234567890',bytes(255)))
#print(hmac_sha256(b'i love yo',bytes(255)))


#key1=hkdf(length, os.urandom(64), salt_key)
#print(key)



