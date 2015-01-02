def histogram(word):
	d=dict()
	for letter in word:
		d[letter]=d.get(letter,0)+1
	return d

def print_hist(word):

	h=histogram(word)
	wordkeys=h.keys()
	wordkeys.sort()

	for i in wordkeys:
		print i, h[i]

print(print_hist('recursive'))
