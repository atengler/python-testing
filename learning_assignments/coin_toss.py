from __future__ import division

from random import randint

trials = 10000
flips = 0

for trial in range(1, trials):
    first_flip = randint(0, 1)
    flips += 1
    while randint(0, 1) == first_flip:
        flips += 1
    flips += 1

print "Average number of coin tosses needed is:", flips / 10000