# program for listing words with no 'forbidden letters' in the file words.txt

# defining a function to check whether given letters are present in the word
def avoids(word,forbidden):
    for letter in forbidden:
        if word.find(letter) != -1:
            return False
    return True


fin = open('/home/dheeraj/think-python/words.txt','r') # opened the file words.txt
for_letters = raw_input("Enter the forbidden letters :- ")
for line in fin:        # for each line in the file
    word = line.strip()
    
    if avoids(word,for_letters) == True: # if forbidden letters not found in the word, print the word
        
        print word



