import collections

def test(x):
	freq = collections.Counter(x)
	for i in freq:
		if '0' in list(freq.elements()):
			return 0
		if freq[i] > 1:
			return 0
	return int(x)

count = 0
for x in range( 1 , 10000):
	pan = str(x)
	y = 2
	while len(pan) < 9:
                z = y * x
                pan += str(z)
                y += 1
	if len(pan) == 9 and test(pan) > 0:
		i = int(pan)
		if i > count:
			count = i

print('The largest concatenated pandigital product is {}!' .format(count))
