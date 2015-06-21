from random import choice

nouns = [ "fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla" ]
verbs = [ "kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles" ]
adjectives = [ "furry", "balding", "incredulous", "fragrant", "exuberant", "glistening" ]
prepositions = [ "against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within" ]
adverbs = [ "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously" ]

def twoUnique(one, list):
	two = choice(list)
	while one == two:
		two = choice(list)
	return two

def threeUnique(one, two, list):
	three = choice(list)
	while one == three or two == three:
		three = choice(list)
	return three

def makePoem():
	noun1 = choice(nouns)
	noun2 = twoUnique(noun1, nouns)
	noun3 = threeUnique(noun1, noun2, nouns)

	verb1 = choice(verbs)
	verb2 = twoUnique(verb1, verbs)
	verb3 = threeUnique(verb1, verb2, verbs)

	adjective1 = choice(adjectives)
	adjective2 = twoUnique(adjective1, adjectives)
	adjective3 = threeUnique(adjective1, adjective2, adjectives)

	adverb1 = choice(adverbs)

	preposition1 = choice(prepositions)
	preposition2 = twoUnique(preposition1, prepositions)

	vowels = ["a","e","i","o","u"]

	if adjective1[0].lower() in vowels:
		aan = "An"
	else:
		aan = "A"

	poem = """{0} {7} {1}

{0} {7} {1} {4} {11} the {8} {2}
{10}, the {1} {5}
the {2} {6} {12} a {9} {3}""".format(aan, noun1, noun2, noun3, verb1, verb2, verb3, adjective1, adjective2, adjective3, adverb1, preposition1, preposition2)

	return poem

print makePoem()