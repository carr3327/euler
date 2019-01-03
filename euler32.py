import collections

def test(x,y,z):
	i = str(x) + str(y) + str(z)
	if len(i) != 9:
		return 1
	freq = collections.Counter(i)
	for k in freq:
		if '0' in list(freq.elements()):
			return 1
		if freq[k] > 1:
			return 1
	return 0

count = []
for n in range( 1 , 50 ):
	for i in range ( 1 , 5000):
		s = n * i		
		if ( test(n,i,s) == 0 ):
			count.append(s)
a = list(set(count))
total = sum(map(int, a))			
print('The sum of all 1-9 pandigital products is {}!' .format(total))

