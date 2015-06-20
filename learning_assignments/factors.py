number=raw_input("Enter a positive integer: ")
try:
	number=int(number)
except:
	print "You must choose single number"

try:
	for i in range(1, number+1): 
		if number % i == 0:
			print i, "is a divisor of", number 
except:
	print "Function failed"