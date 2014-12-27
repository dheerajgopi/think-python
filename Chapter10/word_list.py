def list_words():
    
    
    wordlist=[]
    fin = open('/home/dheeraj/think-python/words.txt')
    for line in fin:
        word=line.strip()
        wordlist.append(word)

    print wordlist

    
