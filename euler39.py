import math
from math import sqrt


def test(x):
	sol = 0
	for a in range(2,int(x/2)):
		for b in range(a+1,int(x/2)):
			for c in range(b+1,a+b):
				if a + b + c == x and a**2 + b**2 == c**2:
					sol += 1

	return sol
count = 0
for x in range(9,1001):
	if test(x) > count:
		count = test(x)
		print(x,count)
