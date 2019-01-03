sum = 0
for i in 1..100
	sum += i **2	
end
sum_square = 0
for j in 1..100
	sum_square += j
end
sum_square = sum_square ** 2
puts sum_square - sum
