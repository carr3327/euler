def test(n):
	x = bin(n)
	y = x[2:]
	if y != y[::-1]:
		return 0
	z = str(n)
	if z != z[::-1]:
		return 0
	return 1

total = 0
for n in range(0,1000001):
	if test(n) == 1:
		total += n
print('The sum of  all palindromic numbers, in base 2 and 10, under one million is {}!' .format(total)) 	
