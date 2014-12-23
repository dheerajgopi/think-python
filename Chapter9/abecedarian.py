# checks if each letter in a word is in alphabetical order

def is_abecedarian(word):

    prvalpbt = 'a'      # initialising a variable for checking with previous alphabet

    for letter in word: # for loop for comparing each letter with the previous alphabet

        if letter < prvalpbt:
            return False
        elif letter >= prvalpbt:
            prvalpbt = letter

    return True
