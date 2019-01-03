def primality(n)
	sqrt = Integer.sqrt(n)
	for i in 2..sqrt
		if n % i == 0
			return 0
		end
	end
return n
end


count = 2
for i in 2..105000
	if count == 10001
		puts i-1
		break
	elsif primality(i) == i
		count+=1
	end
end
