from __future__ import division

from random import random

""" Candidate A has 87% chance of winning in Region 1, 65% chance of winning in Region 2 and 17% chance 
of winning in Region 3. If he wins at 2 or 3 regions, he will win the elections. Calculate overall chance 
of winning of candidate A and candidate B """

candidateA = 0
candidateB = 0

for overall in range(0, 10000):
	if random() <= 0.87:
		region1 = 1
	else:
		region1 = 0
	if random() <= 0.65:
		region2 = 1
	else:
		region2 = 0
	if random() <= 0.17:
		region3 = 1
	else:
		region3 = 0
	if region1 + region2 + region3 > 1:
		candidateA = candidateA + 1
	else:
		candidateB = candidateB + 1

print "Propability of candidate A winning:", str(candidateA / 100) + "%"
print "Propability of candidate B winning:", str(candidateB / 100) + "%"