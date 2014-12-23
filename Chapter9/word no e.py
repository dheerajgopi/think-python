# program for listing words with no 'e' in the file words.txt

# defining a function to check whether 'e' is present in the word
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

fin = open('/home/dheeraj/think-python/words.txt','r') # opened the file words.txt

for line in fin:        # for each line in the file
    word = line.strip()
    
    if has_no_e(word) == True: # if e not found in the word, print the word
        print word


