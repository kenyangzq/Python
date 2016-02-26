f = open("problem4.practice.txt", 'r')
for r in f:
    a = [i for i in list(r) if i != '\n']
    p = [0]*26
    r = 0
    for l in a:
        i = ord(l)-ord('a')
        p[i] += 1
    for k in p:
        if k %2 == 1:
            r+=1
    if r >1:
        print ("no")
    else:
        print ("yes")
