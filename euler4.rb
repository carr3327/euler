def pal(n)
	n =n.to_s 
	if n == n.reverse
		return n
	end
return 0
end

max = 0
for x in 800..999
	for y in 800..999
		result = x*y
		if pal(result) != 0 && result > max
			max = result
		end
	end
end
puts max
