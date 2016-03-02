def k(r):
    a = [0, 1, 1]
    sum = 0
    i = 0
    for j in range(0, 10):
        a[len(a): ] = [a[i] + a[i+1]+a[i+2]]
        i += 1
        if a[-1] >= int(r):
            if a[-1] % 3 == 0:
                sum += a[-1]
        else:
            return sum

f = open("problem6.practice.txt", 'r')
for r in f:
    print (k(r))