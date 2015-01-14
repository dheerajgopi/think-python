# Program for listing anagrams in the wordlist
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

# Sorting anagram list in descending order of number of words formed by a set of words
letter_list.sort(key = lambda x:len(x),reverse = True)

# Displaying the list of anagrams
for i in letter_list:

	print i
