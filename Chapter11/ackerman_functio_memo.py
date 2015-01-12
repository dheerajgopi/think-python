# defining the ackerman function where 'm' and 'n' are positive integers
import timeit

resultdir={}

def ack(m,n):

	if (m,n) in resultdir:
		return resultdir[(m,n)]

    # checking if parameters are integers
	if not isinstance (m,int) or not isinstance(n,int):
       		print "pls enter an integer value"
       		return none

    # checking if parameters are positive integers
   	elif m<0 or n<0:
       		print "pls enter a positive integer"
       		return none

    # defining ackermans functions for various conditions
    	elif m==0:
        	answer = n+1
		resultdir[(m,n)]=answer
        	return answer
    	elif m>0 and n==0:
        	answer = ack(m-1,1)
		resultdir[(m,n)]=answer
        	return answer
    	elif m>0 and n>0:
        	answer = ack(m-1,(ack(m,n-1)))
		resultdir[(m,n)]=answer
        	return answer

print ack(0,1)
print ack(1,0)
print ack(1,2)
print(timeit.timeit("ack(2,3)","from __main__ import ack",number=3))
