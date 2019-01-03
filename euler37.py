from math import sqrt

def test(n):
	if n % 2 == 0:
		return 0
	for num in range(3,int(sqrt(n))+1):
		if n % num == 0 or num * 2 == n:
			return 0
	i = str(n)
	j = str(n)
	total = []
	for a in range(0,len(i)-1):
		a = i[1:]
		i = a
		total.append(int(i))
		for b in range(0,len(j)-1):
			b = j[:-1]
			j = b
			total.append(int(j))
	total.sort()
	for x in total:
		if x == 1:
			return 0
		y = int(sqrt(x))
		for z in range(2, y+1):
			if x % z == 0:
				return 0
	return 1
total = 0
for x in range( 20, 740000):
	if test(x) == 1:
		total += x
print('The sum of primes that are left and right truncatable is {}!' .format(total))
