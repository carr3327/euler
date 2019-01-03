i = 2520
while i < 1000000000
	div = 20
	while div > 0
		if i % div != 0
			break
		elsif div == 1
			puts i
			break
		else
			div-=1
		end
	end
	i+=20
	if div == 1
		break
	end
end

