# function for summing any number of given arguments

def sumall(*args):
	sum=0
	for i in args:
		sum=sum+i
	return sum

print sumall(1,2,3,4)
