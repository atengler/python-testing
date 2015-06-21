def enrollment_stats(list_of_lists):
	enrolled = [enrolled[1] for enrolled in list_of_lists]
	tuition = [tuition[2] for tuition in list_of_lists]
	enrolled_tuition = [ enrolled, tuition ]
	return enrolled_tuition

def median(list_of_numbers):
	list_of_numbers.sort()
	return list_of_numbers[3]

def mean(list_of_numbers):
	numbers_sum = 0
	for x in list_of_numbers:
		numbers_sum = numbers_sum + x
	return numbers_sum / 7

cit = [ "California Institute of Technology", 2175, 37704 ]
harvard = [ "Harvard", 19627, 39849 ]
mit = [ "Massachusetts Institute of Technology", 10566, 40732 ]
princeton = [ "Princeton", 7802, 37000 ]
rice = [ "Rice", 5879, 35551 ]
stanford = [ "Stanford", 19535, 40569 ]
yale = [ "Yale", 11701, 40500 ]

universities = [ cit, harvard, mit, princeton, rice, stanford, yale ]

enrolled_students = enrollment_stats(universities)[0]
tuition = enrollment_stats(universities)[1]

total_students = sum(enrolled_students)
total_tuition = sum(tuition)

print "************************"
print "Total students:", total_students
print "Total tuition: $", total_tuition, "\n"

print "Student mean:", mean(enrolled_students)
print "Student median:", median(enrolled_students), "\n"

print "Tuition mean: $", mean(tuition)
print "Tuition median: $", median(tuition)
print "************************"