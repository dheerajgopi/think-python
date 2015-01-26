# PROJECT GUTENBERG

# Function to split a txt document into list words. the list excludes punctuations, whitespace, and each word is converted to lower case
def stripbook(fin): # Provide the path of the txt document
	import string

	word_list = [(y.translate(None,string.punctuation)).lower() for x in [line.split() for line in fin] for y in x]
   	            # strip punc and change to lower case            for each element in the list of unstripped words

	return word_list

# function to create histogram
def histogram(word):
	d={}
	for x in word:
		d[x]=d.get(x,0)+1
	return d

f = open('/home/dheeraj/repos/think-python/pg47967.txt')

# reading lines until the doc reaches its header (marked by *** at the beginning of line).
for line in f:
	if line.startswith('***'):
		break

listbook = stripbook(f)

print '\nTotal number of words used :- ', len(set(listbook)),'\n'

hist = histogram(listbook)

frq_list =sorted([(y,x) for x,y in hist.iteritems()], reverse = True)

print '20 most frequently used words are :\n'

for i in range(0,20):
	print i+1,'.) ',frq_list[i][1],' ---- ',frq_list[i][0],' times'
print '\n'

# for finding number of words in listbook not available in  words.txt
g = open('/home/dheeraj/repos/think-python/words.txt')

words_list = stripbook(g)
diff = set(listbook) - set(words_list)

for i in diff:
	print i

print '\n\nThe number of words not present in words.txt :- ',len(diff),'\n'
