def F_to_C(F):
	"""Converts degrees Fahrenheit to degrees Celsius"""
	C = (float(F) - 32) * 5 / 9
	return C

def C_to_F(C):
	"""Converts degrees Celsius to degrees Fahrenheit"""
	F = float(C) * 9 / 5 + 32
	return F

conversion_type = raw_input("Press 1 for F to C conversion, press 2 for C to F conversion: ")

if conversion_type == "1":
	fahrenheits = raw_input("Enter degrees Fahrenheit: ")
	print F_to_C(fahrenheits), "degrees Celsius"
elif conversion_type == "2":
	celsiuses = raw_input("Enter degrees Celsius: ")
	print C_to_F(celsiuses), "degrees Fahrenheit"
else:
	print "Next time press either 1 or 2 asshole"