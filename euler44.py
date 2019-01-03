def Pen(n):
	x = (n * ( 3*n -1 ) ) / 2
	return x

pen = []
for x in range( 1 , 2500):
	pen.append(Pen(x))

num = 1000
for z in range( -1 , -num , -1 ):
	for y in range( 1, len(pen)):
		i = pen[z] - pen[y]
		if i <= 0:	
			break 
		if i in pen:
			j = pen[z] + pen[y]
			if j in pen:
				print(i,"it works")
