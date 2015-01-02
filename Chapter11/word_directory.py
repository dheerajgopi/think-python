def word_directory():

	fin = open('/home/dheeraj/think-python/words.txt')
	word_dir=dict()
	i = 0

	for line in fin:

		word=line.strip()
		i+=1
		word_dir[word]=i
	return word_dir

def search(word):

	dictionary=word_directory()
	if word in dictionary:
		return dictionary[word]
	else:
		return False

print(search('humble'))
