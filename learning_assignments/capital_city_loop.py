from capitals import capitals_dict
import random

while True:
	state_list = []
	for state in capitals_dict:
		state_list.append(state)

	question = random.choice(state_list)
	correct_answer = capitals_dict[question]

	given_answer = raw_input("What is the name of capital city of " + question + ": ")

	if given_answer.lower() == correct_answer.lower():
		print "Correct"
		break
	elif given_answer.lower() == "exit":
		print "Goodbye"
		break
	else:
		print "Incorrect"
		continue