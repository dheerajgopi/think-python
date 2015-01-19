import random

def histogram(word):

	d={}

	for letter in word:

		d[letter]=d.get(letter,0)+1

	return d

def choose_from_hist(word):

	a = random.choice(histogram(word).keys())
	return a , histogram(word)[a],'/',len(word)

print choose_from_hist('aabbccd')
