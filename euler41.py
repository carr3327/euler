import collections
from math import sqrt

def is_pan(n):
	freq = collections.Counter(n)
	for i in freq:
		if '0' in list(freq.elements()):
			return 0
		if freq[i] > 1:
			return 0
		if int(i) > len(n):
			return 0 
	return 1 

for x in range(17,987654321): 
	if x % 2 != 0 and is_pan(str(x)) == 1:
		n = int(sqrt(x))+2
		for z in range(3, n):
			if x % z == 0 or z*z == x:
				break
			if z == n - 1:
				print(x)
				break
				
