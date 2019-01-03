import math
import collections

def test(x,y):
	a = str(x)
	b = str(y)
	z = a + b
	sum = x / y 
	i = collections.Counter(z)
	for k in i:
		if a[0] != a[1] and b[0] != b[1] and a[1] != b[1] and b[1] != '0':
			if (i[k] > 1) and (k != 0):
					if int(a[0]) / int(b[1]) == sum: 		
						return 1
	return 0
total = 1
for x in range( 11, 99):
	for y in range( 11, 99):
		z = x / y 
		if ( z < 1 and test(x,y) == 1):	
			total = total * z
sum = round(total,2)
print('The product of the four non-trivial fractions is {}!' .format(sum,"%.2f"))			
