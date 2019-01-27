
data = []
counter=[]

def mean(list):
    return sum(list)/len(list)


def difference(filepath,p):
    index=[]
    difference=[]

    with open(filepath, "rb") as ins:
        for line in ins:
            index.append(int(line))


    for i in xrange(0,len(index)):
        if i==len(index)-1:
            break
        else:
            difference.append(index[i+1]-index[i])

    with open("period%s_diff.txt"%p, "w") as f:
        for item in difference:
            f.write("%s\n" % item)

    print(max(difference),min(difference))
    print(mean(difference) )




def count(list,min,max):
    ctr = 0
    for x in list:
        if min <= x < max:
            ctr += 1
    return ctr



def main():
    for i in range(2, 7):
        difference("period%s.txt" % i, i)

    for i in range(2, 7):
        with open("period%s_diff.txt" % i, "rb") as ins:
            for line in ins:
                data.append(int(line))
    for i in range(0,17):
        counter.append(count(data,0+5000*i,5000+5000*i))
    for item in counter:
        print(item)
    print (sum(counter))
    print(len(data))
main()
