# Finding reverse pair of every word in the word list

# Creating the sorted word list
wordlist =sorted([x.strip() for x in open('/home/dheeraj/repos/think-python/words.txt')])

# Function for binary search
def binary(word):

	# first = 1st index in the list..initially 0
	first = 0

	# last = last index in the list..initially len(list)
	last = len(wordlist)

	# loop for changing first and last index
	while first < last:

		middle = (first + last)/2
		midval = wordlist[middle]

		# first index changed to middle index if word is in the second half of list
		if midval < word:

			first = middle + 1

		# last index changed to middle index if word is in the first half of list
		elif midval > word:

			last = middle

		# if first index == last index return the index
		else:

			return middle

	# if not in the list...
	return -1

# Creating list of reverse pairs 
pairlist = [tuple(sorted((x,x[::-1]))) for x in wordlist if binary(x[::-1]) != -1]

# Removing duplicates
print set(pairlist)
print len(set(pairlist))
