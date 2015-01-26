# MARKOV ANALYSIS

import random

def stripbook(fin): # Provide the path of the txt document
	import string

	word_list = [y.translate(None,string.whitespace) for x in [line.split() for line in fin] for y in x]

	return word_list

def markov(word,length=2):
	d={}
	for x in range(0,len(word)-2):
		d[word[x]] = word[x+1]
	return d

f = open('/home/dheeraj/repos/think-python/emma.txt')

# reading lines until the doc reaches its header (marked by *** at the beginning of line).
for line in f:
	if line.startswith('*END*'):
		break

listbook = stripbook(f)

markovdict = markov(listbook)

wordlist = markovdict.keys()

a=random.randrange(0,len(wordlist))

sentence = [wordlist[a]]

i=0

while i < 100:

	sentence.append(markovdict[sentence[-1]])

	i += 1

final=''
for i in sentence:
	final = final + ' ' +i

print final
