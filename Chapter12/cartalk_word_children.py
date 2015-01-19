# Defining a function accepting a string as input & returning a list of child words of that string
def word_children(word):

	# Initialising a list for storing the result
	child_list = []

	# Loop for creating the child word list
	for i in word:

		list_word = list(word)
		list_word.remove(i)
		child_word = ''.join(list_word)
		child_list.append(child_word)

	# Returns the child word list
	return child_list

fin = open('/home/dheeraj/repos/think-python/word.txt')
dict_word = {}

for line in fin:

	word = line.strip()
	dict_word[word]=word


fin = open('/home/dheeraj/repos/think-python/word.txt')

templist = []
for line in fin:

	word = line.strip()
	word_child = word_children(word)
	finallist = []

	for i in word_child:
		if i in dict_word:

			abc = i
			templist.append(abc)
			print templist
