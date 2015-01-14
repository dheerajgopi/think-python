# Program for scanning a wordlist and returning the most frequently used lettersin descending order

import operator

# Defining a function for accepting a word & returning a list of tuples with letters used and its frequency
def most_frequent(wrd):

	d={}
	for letter in wrd:
		d[letter] = d.get(letter,0)+1
	letter_freq = d.items()
	letter_freq.sort(key = operator.itemgetter(1),reverse=True)
	return letter_freq

# Opening the file containing the word list
fin = open("/home/dheeraj/repos/think-python/words.txt")

total_freq = {}

# Loop for scanning each word in the file and building a histogram
for line in fin:
	word = line.strip()
	freq_list = most_frequent(word)
	freq_dict = dict(freq_list)

	for i in freq_dict:
		total_freq[i]=total_freq.get(i,0)+freq_dict[i]

# Sorting the histogram in descending order
letter_list = total_freq.items()
letter_list.sort(key=operator.itemgetter(1),reverse = True)

# Loop for printing the histogram
print 'letter ---- frequency'
for i in letter_list:

	print '  ',i[0],'       ',i[1]
