fin = open('/home/dheeraj/repos/think-python/word.txt')
dict_word = {}

for line in fin:

	word = line.strip()
	dict_word[word]=word

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

def test(word):

	child_list = word_children(word)
	print child_list
	for i in child_list:
		if i in dict_word:
			print i
			return test(i)


print test('sprite')
