
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
# alt_statekey = bytes(os.urandom(32))

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


def GGF(input_bits,data):
    start_time = time.time()
    key=key_initial
    #CT2=G_0+G_1
    #print(b64encode(CT2))
    #print("duh")

    for i in range (0,input_bits+1):
        CT = aes_ctr(key, data)
        #print (b64encode(CT))
        G_0, G_1 = CT[:len(CT) / 2], CT[len(CT) / 2:]
        print(b64encode(CT))
        if random.choice([True, False]):
            key=G_1
            print(b64encode(G_1))
        else:
            key=G_0
            print(b64encode(G_0))
        #print(b64encode(key))
        print(i)
    print ("%s seconds" % (time.time() - start_time))
    return key

def main():
    for i in range (1,128):
        start_time = time.time()
        GGF(i,salt_key)
        print ("%s seconds for %s bits GGF " % ((time.time() - start_time),i))

GGF(128,salt_key)



