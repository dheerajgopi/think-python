# Program for listing metathesis pairs in the wordlist

def metathesis_pair(word1,word2):

	# Initialising a variable 'diff'
	diff = 0
	
	# Returns False if word length is different
	if len(word1) != len(word2):

		return False

	# Loop for comparing strings 
	for i in range (0,len(word1)):

		# increment diff by 1 for each swap
		if word1[i] != word2[i]:

			diff += 1

	# Returns True if only two letters are swapped else False
	if diff == 2:

		return True

	else:

		return False

# Opening the wordlist file and initialising empty dict and list
fin = open('/home/dheeraj/repos/think-python/words.txt')
letter_dict = {}
letter_list = []

# Creating dictionary with set of letters as key and list of words formed by the letters as its value
for line in fin:

	word = line.strip()
	word_tuple = tuple(sorted(word))
	letter_dict.setdefault(word_tuple,[]).append(word)

# Creating a list by including only anagrams i.e excluding single word values
for key in letter_dict:

	if len(letter_dict[key]) > 1:

		letter_list.append(letter_dict[key])

# Loop for printing the metathesis pairs in the wordlist
# Initialising the var count for counting the number of metathesis pairs
count = 0

# Checking each anagram set for metathesis pairs
for i in letter_list:

	for j in i:

		for k in i:
			
			# Checking if metathesis pair
			mp = metathesis_pair(j,k)

			# If True print the metathesis pair and increment count by 1
			if mp == True:
				print j,k
				count += 1

		# Removing list element to prevent duplicates
		i.remove(j)

# Displaying the total count of metathesis pairs
print '\nTotal number of metathesis pairs are :- ',count,'\n'
