def k(p):
    if p<42:
        return False
    if p==42:
        return True
    if p%2==0:
        return k(p/2)
    if p%3==0:
        a=(p%10)*(p%100/10)
        return k(p-a-1)
    if p%5==0:
        return k(p-42)
    return k(p-1)

f = open("problem2.practice.txt", 'r')
for r in f:
    if k(int(r)):
        print ("yes")
    else:
        print ("no")