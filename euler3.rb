def factors(n)
	i = Integer.sqrt(n) 
	top = 0
	x = 2
	while x < i
		if n % x == 0
			n = n / x
			if prime(x) == x
				top = x
			end
			x += 1
		else
			x += 1
		end
	end
return top 
end

def prime(n)
	j = Integer.sqrt(n)
	k = 2
	while k < j
		if n % k == 0
			return 0
			break
		else
			k+=1
 	       	end
	end
return n
end

puts factors(600851475143)
