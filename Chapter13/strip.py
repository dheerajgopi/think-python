# Function to split a txt document into list words. the list excludes punctuations, whitespace, and each word is converted to lower case

def stripbook(fin = open('/home/dheeraj/repos/think-python/pg47967.txt')): # Provide the path of the txt document
	import string

	word_list = [(y.translate(None,string.punctuation)).lower() for x in [line.split() for line in fin] for y in x]
	     # strip punc and change to lower case            for each element in the list of unstripped words

	return word_list
