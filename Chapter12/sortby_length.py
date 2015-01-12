def sort_by_length(words):
	t=[]
	for word in words:
		t.append((len(word),word))
	
	t.sort(reverse=True)
	
	res=[]

	for length,word in t:
		print (t[length])
		res.append(word)
	return res


a=('a','ab','fe','cd','ad','ada','adssada')

print(sort_by_length(a))

