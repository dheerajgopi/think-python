

def rotn(word,n):
    rotword = '' # initialising empty string for result

    for letter in word:
        
        rotword = rotword + rotl(letter,n) # adding each letter to form final word
	return rotword

#function for converting a letter to its rotated letter
def rotl(l,n):

    rotletter = ord(l)+n    # converting each letter into numeric code and adding it with n

    if l.isupper():         # checking if letter is uppercase

        if rotletter > 90:  # cyclic addition
            rotletter = rotletter - 26
        elif rotletter < 65:
            rotletter = rotletter + 26

    elif l.islower():       # checking if lowercase

        if rotletter > 122: #cyclic addition
            rotletter = rotletter - 26
        elif rotletter < 97:
            rotletter = rotletter + 26

    return chr(rotletter)   # returning the rotated character


fin=open("/home/dheeraj/repos/think-python/words.txt")
wrdict={}
for line in fin:
	word=line.strip()
	wrdict[word]=word

for i in range (1,14):
	rword=rotn('cheer',i)

if rword in wrdict:
	print rword

