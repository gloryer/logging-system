import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import math

def bar():

    n_groups = 5

    means_men = (26083, 26083, 25955, 25764, 25891)
    # #std_men = (2, 3, 4, 1, 2)
    #

    means_women =(11014,10923 , 11014, 10991, 10923)



    fig, ax = plt.subplots()


    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.5
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, means_men, bar_width,
                    alpha=opacity, error_kw=error_config,
                    label='Our Scheme')

    rects2 = ax.bar(index + bar_width, means_women, bar_width,
                    alpha=opacity, color='orange',
                    error_kw=error_config,
                    label='SLiC')



    ax.set_xlabel('Trial')
    ax.set_ylabel('Log Rate (events/s)')
    ax.set_title('Logging Rate Comparison on the Window Computer')
    ax.set_xticks(index + bar_width / 2)
    # ax.set_yticks()
   # print(list(np.arange(0.5, 2.6, 0.5)))
    #plt.yticks( list(range(0, 26000, 5000)),["0"]+["%.1fx$10^{4}$"%k for k in np.arange(0.5, 2.6, 0.5)])
    plt.yticks( list(range(0, 26000, 5000)),["0"]+["%d K"%k for k in np.arange(5, 26, 5)])
    #print("Im here")
    ax.set_xticklabels(('1', '2', '3', '4', '5'))
    ax.set_ylim((0,32000))

    for rect in rects1:
        height = rect.get_height()
        plt.annotate(height,xy=(rect.get_x() + rect.get_width() / 2, height+2),ha='center', va='bottom')

    for rect in rects2:
        height = rect.get_height()
        plt.annotate(height,xy=(rect.get_x() + rect.get_width() / 2, height+2),ha='center', va='bottom')
    #plt.annotate('mean value of interval : %d' % meandata, xy=(meandata, 90), xytext=(25000, 90),
                 #arrowprops=dict(facecolor='black', shrink=0.10))

    ax.legend()

    #fig.tight_layout()

    plt.show()





def histogram():
    data = []

    for i in range(2, 7):
        with open("period%s_diff.txt"%i, "rb") as ins:
            for line in ins:
                data.append(int(line))

    #bins=[2, 2**2, 2**3, 2**4,2**5,2**6,2**7,2**8,2**9,2**10,2**11,2**12,2**13,2**14,2**15,2**16,2**17]

    bins = np.arange(math.ceil(min(data)),math.floor(max(data)), 5000)
    #ax = plt.subplots()
    #     bins = np.linspace(math.ceil(min(data)),
                       #                    math.floor(max(data)),
                       #                    30) # fixed number of bins

    #plt.xlim([min(data)-5, max(data)+5])

    plt.hist(data, bins=bins, alpha=0.5,edgecolor='black',linewidth=1)

    dataNP = np.array(data)
    meandata = dataNP.mean()
    plt.plot([meandata, meandata], [0, 90], color='blue', linestyle="--")
    plt.plot([16384, 16384], [0, 90], color='red', linestyle="--")

    plt.title('Distribution of time intervals in every state control key update')
    plt.xlabel('time intervals (bin size is 5000 events)')
    plt.ylabel('count')

    plt.annotate('mean : x=%d events'%meandata, xy=(20000,85),color='blue')
    plt.annotate('theoretical interval value: %d events' % 16384, xy=(20000, 80),color='red')
    plt.annotate("24%", xy=(2500, 74),ha='center', va='bottom')
    plt.annotate("17%", xy=(8800, 53), ha='center', va='bottom')
    plt.annotate("15%", xy=(12500, 47), ha='center', va='bottom')
    plt.annotate("12%", xy=(17500, 39), ha='center', va='bottom')
    plt.annotate("9%", xy=(22500, 27), ha='center', va='bottom')
    plt.annotate("6%", xy=(27500, 19), ha='center', va='bottom')
    plt.annotate("5%", xy=(33500, 17), ha='center', va='bottom')
    plt.annotate("2%", xy=(37500, 7), ha='center', va='bottom')
    plt.annotate("3%", xy=(45500, 9), ha='center', va='bottom')
    #plt.annotate("3%", xy=(47500, 9), ha='center', va='bottom')
    plt.annotate("2%", xy=(53500, 7), ha='center', va='bottom')
    plt.annotate("0.7%", xy=(60000, 3), ha='center', va='bottom')
    #plt.annotate("0.7", xy=(62500, 3), ha='center', va='bottom')
    plt.annotate("0%", xy=(67500, 1), ha='center', va='bottom')
    plt.annotate("0.3%", xy=(75500, 2), ha='center', va='bottom')
    #plt.annotate("0.3", xy=(77500, 2), ha='center', va='bottom')


    plt.show()


def bar_PI():

    n_groups = 5

    means_men = (3173, 3222, 3287, 3231, 3281)
    # #std_men = (2, 3, 4, 1, 2)
    #

    means_women =(1327,1324 ,1348, 1332, 1316)



    fig, ax = plt.subplots()


    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.5
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, means_men, bar_width,
                    alpha=opacity, error_kw=error_config,
                    label='Our Scheme')

    rects2 = ax.bar(index + bar_width, means_women, bar_width,
                    alpha=opacity, color='orange',
                    error_kw=error_config,
                    label='SLiC')



    ax.set_xlabel('Trial')
    ax.set_ylabel('Log Rate (events/s)')
    ax.set_title('Logging Rate Comparison on the Raspberry Pi')
    ax.set_xticks(index + bar_width / 2)
    # ax.set_yticks()
   # print(list(np.arange(0.5, 2.6, 0.5)))
    #plt.yticks( list(range(0, 26000, 5000)),["0"]+["%.1fx$10^{4}$"%k for k in np.arange(0.5, 2.6, 0.5)])
    #plt.yticks( list(range(0, 26000, 5000)),["0"]+["%d K"%k for k in np.arange(5, 26, 5)])
    #print("Im here")
    ax.set_xticklabels(('1', '2', '3', '4', '5'))
    ax.set_ylim((0,4500))

    for rect in rects1:
        height = rect.get_height()
        plt.annotate(height,xy=(rect.get_x() + rect.get_width() / 2, height+2),ha='center', va='bottom')

    for rect in rects2:
        height = rect.get_height()
        plt.annotate(height,xy=(rect.get_x() + rect.get_width() / 2, height+2),ha='center', va='bottom')
    #plt.annotate('mean value of interval : %d' % meandata, xy=(meandata, 90), xytext=(25000, 90),
                 #arrowprops=dict(facecolor='black', shrink=0.10))

    ax.legend()

    #fig.tight_layout()

    plt.show()


#histogram()
bar_PI()