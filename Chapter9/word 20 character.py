# program for listing words above 20 characters in the file words.txt

fin = open('/home/dheeraj/think-python/words.txt','r') # opened the file words.txt

for line in fin:        # for each line in the file
    word = line.strip()
    
    if len(word) > 20:
        print word
