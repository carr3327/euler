def fib(n)
	count = 0
	prev = 0
	last = 1
	total = 0
	while count < n do
		total = prev + last
		prev = last 
		last = total
		count +=1
	end

return total
end

total = 0
i = 1
while fib(i) < 4000000
	if fib(i) % 2 == 0
		total += fib(i) 
		i +=1
	else
		i+=1
	end
end
puts total
