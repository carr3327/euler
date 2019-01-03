x = 1 
total = 0
while x < 1000
	if x % 3 == 0
		total += x 
		x += 1
	elsif x % 5 == 0
		total += x
		x +=1
	else
		x +=1
	end
end
puts total
