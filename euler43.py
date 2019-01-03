from itertools import permutations
def is_div(n):
	x = str(n)
	if int(x[0]) == 0:
		return 0
	if int(x[:2]) != 14 and int(x[:2]) != 41:
		return 0
	if int(x[5]) != 5:
		return 0
	if int(x[4:10]) != 357289 and int(x[4:10]) != 952867:
		return 0
	for y in range(1,len(x)-2):
		num = int(x[y:y+3])
		prime = [2,3,5,7,11,13,17]
		if len(str(num)) == 3:
			z = prime[y - 1]
			if num % z != 0:
				return 0
	return 1 
sum = 0
x = [1,2,3,4,5,6,7,8,9,0]
for p in permutations(x):
	y = ''.join(str(n) for n in p)
	if is_div(y) == 1:
		sum += int(y)
		print(y,sum)
print(sum)

			
