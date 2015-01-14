# for sorting a list according to the length of its elements. elements of same length are sorted randomly

import random

def sort_by_length(words):

	t=[]

	# creating a list 't' with tuples elements.tuple consist of length, random number and word
	for word in words:
		t.append((len(word),random.random(),word))
	
	# sorting the list 't'
	t.sort(reverse=True)

	# initialised a list for storing result	
	res=[]

	# appending the words to the result list
	for length,rnum,word in t:
		res.append(word)
	return res


a=('a','ab','fe','cd','ad','ada','adssada')

print(sort_by_length(a))

