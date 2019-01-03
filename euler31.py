coins = [1,2,5]
target = 5

ways = [1] + [0]*target

##for a in coins:
	##for i in range(a , target+1):
		##ways[i] += ways[i-a]
		##print(ways)
print(ways[target])
