def invest(amount, rate, time):
	i=1
	multiplier=rate+1
	print "principal amount: $"+str(amount)
	print "annual rate of return:", rate
	while (i<time+1):
		amount=amount*multiplier
		print "year "+str(i)+": $"+str(amount)
		i=i+1

def invest2(amount, rate, time):
	multiplier=rate+1
	print "principal amount: $"+str(amount)
	print "annual rate of return:", rate
	for i in range(1, time+1):
		amount=amount*multiplier
		print "year "+str(i)+": $"+str(amount)

invest2(2000, 0.025, 5)