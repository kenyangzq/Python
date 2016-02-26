
def k(p):
    r = 0
    for l in p:
        if l == 'a':
            r += 2
        if l == 'd':
            r -= 1
        if l == 'm':
            r *= 2
        if l == 'o':
            print (r)
            return

f = open("problem1.practice.txt", 'r')
for row in f:
    k(list(row))

