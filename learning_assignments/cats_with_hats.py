cats = {}

for x in range(1,101):
	cats[x] = 0

for x in range(1,101):
	for y in range(1,101):
		if y % x == 0:
			if cats[y] == 0:
				cats[y] = 1
			else:
				cats[y] = 0

print "Cats with hats are:"

for x in cats:
	if cats[x] == 1:
		print "Cat #" + str(x)