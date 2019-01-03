path = '/home/bill/Euler/euler42.txt'

def alpha(n):
	b = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	sum = 0
	for i in n: 
		sum += int(b.find(i))
	return sum



t_num = []
for n in range(1,55):
	y = int((n*n + n)/2)
	t_num.append(y)
text = open(path, 'r')
word = []
word = text.read().replace('"', '').split(',')
count = 0 
for x in range(0,len(word)):
	if alpha(word[x]) in t_num:
		print(word[x],alpha(word[x]))
		count += 1
text.close()
print(count)

