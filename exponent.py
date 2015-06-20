from __future__ import division

base = raw_input("Enter a base: ")
base = base.replace(",", ".")
exponent = raw_input("Enter an exponent: ")
exponent = exponent.replace(",", ".")

print base, "to the power of", exponent, "=", float(base) ** float(exponent)