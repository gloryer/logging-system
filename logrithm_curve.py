
import os

import time
from Crypto.Cipher import AES
import random
import matplotlib.pyplot as plt


key_initial = bytes(os.urandom(16))
statekey_initial = bytes(os.urandom(16))
salt_key =bytes(os.urandom(32))

y=[]

def aes_ctr(key,data):
    cipher = AES.new(key, AES.MODE_CTR)

    nonce = cipher.nonce
    encrypted = cipher.encrypt(data)


    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

    return encrypted


def GGF(input_bits,data):
    start_time = time.time()
    key=key_initial


    for i in range (0,input_bits+1):
        CT = aes_ctr(key, data)
        #print (b64encode(CT))
        G_0, G_1 = CT[:len(CT) / 2], CT[len(CT) / 2:]
        #print(b64encode(CT))
        if random.choice([True, False]):
            key=G_1
            #print(b64encode(G_1))
        else:
            key=G_0
            #print(b64encode(G_0))
        #print(b64encode(key))
    y.append(time.time() - start_time)
    print("%s for input %s bits" %(time.time() - start_time,input_bits))
    return key

def main():
    for i in range (1,129):
        GGF(i,salt_key)


    draw_multiple_points(y)
        #print ("%s seconds for %s bits GGF " % ((time.time() - start_time),i))

#GGF(128,salt_key)




def draw_multiple_points(y_number_list):

    # x axis value list.
    x_number_list = []
    for i in range(1,129):
        x_number_list.append(i)

    # y axis value list.


    # Draw point based on above x, y axis values.
    plt.scatter(x_number_list, y_number_list, s=10)
    #plt.plot(x_number_list, y_number_list, linewidth=3)

    # Set chart title.
    plt.title("GGF Time  ")

    # Set x, y label text.
    plt.xlabel("Input Bits")
    plt.ylabel("Running Time (s)")
    plt.show()


main()



