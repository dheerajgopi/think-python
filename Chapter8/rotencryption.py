# code for encrypting a word by rotating each letter by n times


def rotn(word,n):
    rotword = '' # initialising empty string for result

    for letter in word:
        
        rotletter = ord(letter)+n   # converting each letter into numeric code and adding it with n

        if rotletter > 122:         # for cyclic addition between 97(a) and 122(z)
            rotletter = rotletter - 26
        elif rotletter < 97:
            rotletter = rotletter + 26

        rotword = rotword + chr(rotletter) # adding each letter to form final word

    print rotword       # printing final rotated word
