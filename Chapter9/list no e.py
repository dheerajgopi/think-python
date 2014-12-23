# program for listing words with no 'e' in the file words.txt

# defining a function to check whether 'e' is present in the word
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

fin = open('/home/dheeraj/think-python/words.txt','r') # opened the file words.txt
no_e_word = 0.0
total = 0.0
for line in fin:        # for each line in the file
    word = line.strip()
    total += 1
    if has_no_e(word) == True: # if e not found in the word, print the word
        no_e_word += 1
        print word

percentage = (no_e_word/total)*100

print ("no. of words without 'e' :- ",no_e_word)
print ("total no. of words:- ",total)
print ('percentage :- ',percentage)

