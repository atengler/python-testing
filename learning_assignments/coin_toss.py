from __future__ import division

from random import randint

trials = 10000
flips = 0

"""Average number of coin tosses needed to get different result than we got at first toss. 
For example when first coin toss results in heads and second in tails, there were two coin tosses needed.
If first coin toss results in tails, second in tails and third in heads, we needed three coin 
tosses to get different result etc."""

for trial in range(1, trials):
    first_flip = randint(0, 1)
    flips += 1
    while randint(0, 1) == first_flip:
        flips += 1
    flips += 1

print "Average number of coin tosses needed is:", flips / 10000