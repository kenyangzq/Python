f = open("problem3.practice.txt", 'r')
for r in f:
    b = [int(i) for i in list(r) if i != "\n"]
    sum = []
    for i in range(0, len(b)-1):
        sum[len(sum):] = [b[i+1] - b[i]]
    print (sum)
    # for i in range(0,len(sum)):
        # if
