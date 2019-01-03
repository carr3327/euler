from math import sqrt

def test(x):
	i = str(x)
	total = []
	for j in i:
		j = i[1:] + i[0]
		i = j
		total.append(int(i))
	for k in total:
		a = int(sqrt(k))
		if k % 2 == 0 and k > 2:
			return 0
		for b in range(2,a+1):
			if k % b == 0:
				return 0
	return 1


count = 0
for x in range(2, 1000000):
	if test(x) == 1:
		count += 1
print('There are {} circular primes below one million!' .format(count))
