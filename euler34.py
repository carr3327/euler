from math import factorial

def test(x):
	y = str(x)
	total = 0
	for a in range(0,len(y)):
		b = int(y[a])
		total += factorial(b)
		if total == x:
			return 1
	return 0

total = 0
for x in range(15, 41000):
	if test(x) == 1:
		total += x
print('The sum is {}!' .format(total))
