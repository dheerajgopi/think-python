# function for finding if there are double letters in succession 3 times

def triple_double(word):

# returns True if length of word is less than 6

	if len(word)<6:
		return False

# returns True if there are 3 consecutive double words

	for i in range(0,len(word)-5):	# stops checking at 6th character before the last letter

		if word[i]==word[i+1]:	# returns True if there are 3 consecutive double letters
			if word[i+2]==word[i+3]:
				if word[i+4]==word[i+5]:
					return True

	return False

# listing words with 3 consecutive double letters

fin = open('/home/dheeraj/think-python/words.txt') # opening words.txt
wcount=0                # initialising word count

for line in fin:        # for each word in the file 'triple_double' function is called

	wrd=line.strip()
	
	if triple_double(wrd) is True:  # if function returns True its printed and count is increased by 1
		print wrd
		wcount+=1

print 'Number of words with 3 consecutive double letters is :- \n',wcount	
