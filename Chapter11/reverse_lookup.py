def rev_lookup(d,v):

	lstkeys=[]
	for i in d:
		if d.get(i)==v:
			lstkeys.append(i)
	return lstkeys

e={'a':1,'b':2,'c':2,'d':3}

print(rev_lookup(e,4))

