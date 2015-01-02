def list_words():
    
    
    wordlist=[]
    fin = open('/home/dheeraj/think-python/words.txt')
    for line in fin:
        word=line.strip()
        wordlist.append(word)
    print len(wordlist)
def list_words2():

    
    wordlist2=[]
    fin2 = open('/home/dheeraj/think-python/words.txt')

    for line in fin2:
        word2=line.strip()
        wordlist2=wordlist2+[word2]

import timeit
t=timeit.Timer("list_words()", "from __main__ import list_words")
print "time for append algorithm"
print(t.timeit(2))
    
t2=timeit.Timer("list_words2()", "from __main__ import list_words2")
print "time for t=t+[x] algorithm"
print(t2.timeit(1))
