dec = '.123456789'
x = 10
while len(dec) < 1000001:
	y = str(x)
	dec += y 
	x += 1	

x = 1
place = '1'
sum = 1
while x < 8:
	y = int(place)
	sum *= int(dec[y])
	place += '0'
	x += 1 
print(sum)
