import math

def prime(a):
	if a < 0:
		a = a * -1
	elif a == 1:
		return False
	root = int(math.sqrt(a)) + 1
	for i in range(2,root):
		if a%i == 0:
			return False
	return True

def factorial(a):
	if a == 1 or a == 0:
		return 1
	elif a < 0:
		print "%d is invalid" % a
	else:
		return a * factorial(a-1)

def toBase2(a):
	base2 = 0
	i = 1
	while a != 0:
		base2 += (a % 2) * i
		i *= 10
		a /= 2
	return base2

def reverse(a):
	st1 = ""
	while a != 0:
		st1 = st1 + str(a%10)
		a = a / 10
	return int(st1)

def power(a, b):
	n = 1
	for i in range(1,b+1):
		n *= a
	return n

def combination(n, r):
	return factorial(n) / factorial(r) / factorial(n-r)






# problem 22

def problem22():
	with open("names.txt") as names:
		here = names.read()
		there = here.split("\",\"")
		length = len(there)
		there[0] = there[0][1:]
		there[length-1] = there[length-1][:len(there[length-1])-1]

		there = sorted(there)
		sumup = 0

		for i in range(0, length):
			word = there[i]
			score = 0
			for j in range(0,len(word)):
				score += ord(word[j]) - ord("A") + 1
			sumup += score * (i+1)
		print sumup


# problem 24

def problem24():
	count = 725760
	i = 203456789
	while count < 1000000:
		if permute(i):
			count += 1
		i += 9
	print i

def permute(a):
	num = [0, 2, 3, 4, 5, 6, 7, 8, 9]
	numa = []
	while a != 0:
		numa.append(a%10)
		a = a / 10
	numa = sorted(numa)
	return (num == numa)


# problem 27

def problem27():
	max_num = 1
	max_a = 0
	max_b = 0

	for a in range(-1000, 1000):
		for b in range(-1000,1000):
			count = 0
			i = 0
			while prime(fomular(i, a, b)):
				count += 1
				i += 1
			if count > max_num:
				max_num = count
				max_a = a
				max_b = b
		
	print "The max number of consecutive prime is %d, when a equals %d, b equals %d" % (max_num, max_a, max_b)
	print "The product of a and b is %d" % (max_a * max_b)

def fomular(n, a, b):

	return n*n+n*a+b


# problem 28

def problem28():
	sum = 0
	for i in xrange(0,501):
		sum = sum + 4*i*i+i+1

	sum = 4*sum - 3
	print sum


# problem 30

def problem30():
	sumup = 0
	for i in xrange(3,10000000):
		if digitPower(i):
			sumup += i
			print i
	print sumup

def digitPower(a):
	number = a
	digit_sum = 0
	while(a != 0):
		k = a % 10
		digit_sum += k*k*k*k*k
		a = a/10
	return (digit_sum == number)


# problem 33

# def problem33():
	


# problem 34

def problem34():
	sumup = 0
	for i in range(3,10000000):
		if digitFactorial(i):
			print i
			sumup += i
	print sumup

def digitFactorial(a):
	number = a
	digit_sum = 0
	while a != 0:
		i = a % 10
		digit_sum += factorial(i)
		a = a/10
		if digit_sum > number:
			return False
	return (number == digit_sum)


# problem 35

def problem35():
	count = 0
	for i in range(1,1000000):
		if circular(i):
			count += 1
	print "There are %d circular primes below one million." % count

def circular(a):
	if a < 10:
		return prime(a)

	k = a
	if not prime(k):
		return False
	b = str(k / 10)
	c = str(k % 10)
	k = int(c + b)
	while k != a:
		if not prime(k):
			return False
		b = str(k / 10)
		c = str(k % 10)
		k = int(c + b)
	return True


# problem 36

def problem36():
	sumup = 0
	for i in range(0, 1000000):
		if palindromic(i) and palindromic(toBase2(i)):
			print i
			sumup += i
	print sumup

def palindromic(a):
	st1 = ""
	st2 = ""
	while a != 0:
		st1 = str(a%10) + st1
		st2 = st2 + str(a%10)
		a = a / 10
	return (st1 == st2)


# problem 37

def problem37():
	sumup = 0
	count = 0
	i = 10
	while count < 11:
		if truncatable(i):
			count += 1
			print "i is %d and count is %d" % (i, count)
			sumup += i
		i += 1
	print sumup

def truncatable(a):
	b = reverse(a)
	while a != 0:
		if not prime(a) or not prime(reverse(b)):
			return False
		a = a/10
		b = b/10
	print "It's truncatable."
	return True


# problem 41

def problem41():
	largest = 0
	for i in range(7623451,7654321):
		if prime(i) and pandigital(i):
			if i > largest:
				print i
				largest = i
	print largest

def pandigital(a):
	d = int(math.ceil(math.log10(a)))
	num = []
	while a != 0:
		num.append(a%10)
		a = a/10
	num = sorted(num)

	if num[0] == 0:
		return False

	if num[d-1] > d:
		return False

	for i in range(0,d-1):
		if num[i] == num[i+1]:
			return False
	return True


# problem 42

def problem42():
	count = 0
	with open("42words.txt") as words:
		word = words.read()
		here = word.split("\",\"")
		length = len(here)
		for i in range(1,length):
			p = here[i]
			sumup = 0
			for j in range(0, len(p)):
				k = ord(p[j]) - ord("A")+1
				sumup += k
			if triangle(sumup):
				print p
				count += 1

	print count+1

def triangle(a):
	k = int(math.floor(math.sqrt(2*a)))
	return (2*a == k*(k+1))


# problem 44

def problem44():
	d = 1000000
	for i in xrange(1, 10000):
		if pentagon(i):
			for j in xrange(i+1, i+d):
				if pentagon(j):
					k = j - i
					if pentagon(k) and pentagon(i+j):
						d = k
						print k
				
	print d

def pentagon(a):
	k = int(math.ceil(math.sqrt(6*a)))
	return (6*a == k*(k-1) and k%3 == 0)


# problem 45

def problem45():
	for i in xrange(1,100000):
		a = i * (3 * i -1) / 2
		if hexagonal(a):
			print a

def hexagonal(a):
	k = int(math.floor(math.sqrt(2*a)))
	return (2*a == k*(k+1) and k%2 == 1)


# problem 46

def problem46():
	smallest = 0
	i = 99
	while smallest == 0:
		if not prime(i):
			if not check(i):
				smallest = i
		i += 2
	print smallest
		
def check(a):
	for i in range(1, int(math.floor(math.sqrt(a/2)))):
		if a % i != 0:
			if prime(a - 2*i*i):
				return True
	return False


# problem 48

def problem48():
	sumup = 0
	for i in range(1, 1001):
		sumup += power(i,i)
	print sumup


# problem 49

def problem49():
	for i in range(1000,10000):
		if prime(i):
			for j in range(i+1,9999):
				k = (i+j)/2
				if prime(j) and prime(k) and permutation(i,k,j):					
					print "The sequence are %d, %d and %d" % (i, k, j)

def permutation(a, b, c):
	numa = []
	numb = []
	numc = []
	while a != 0:
		numa.append(a%10)
		numb.append(b%10)
		numc.append(c%10)
		a = a/10
		b = b/10
		c = c/10

	numa = sorted(numa)
	numb = sorted(numb)
	numc = sorted(numc)

	if numa == numb and numb == numc:
		return True
	return False


# problem 53

def problem53():
	count = 0
	for i in xrange(1,101):
		for j in xrange(0,i+1):
			if combination(i,j) > 1000000:
				count += 1
	print count


# problem 56

def problem56():
	a = 0
	b = 0
	maxsum = 0
	for i in xrange(1,100):
		for j in xrange(1,100):
			k = digitsum(power(i,j))
			if k > maxsum:
				a = i
				b = j
				maxsum = k

	print "The maximum digit sum is %d, which is %d ^ %d." % (maxsum, a, b)

def digitsum(a):
	sumup = 0
	while a != 0:
		sumup += a%10
		a = a/10
	return sumup


# problem 357

def problem357():
	sum = 0
	for i in xrange(1,100000000):
		if divisor_prime(i):
			sum += i
			print i
	print sum

def divisor_prime(a):
	for i in xrange(1,int(math.ceil(math.sqrt(a)))+1):
		if a % i == 0:
			if not prime(i+a/i):
				return False
	return True




x = int(raw_input("integer 1"))
y = int(raw_input("integer 1"))

i = 1
while (ceil(i*x) == ceil(i*y)):
	i += 1
print i




