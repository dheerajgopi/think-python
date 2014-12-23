def uses_all(word,alphabets):
    for letter in alphabets:
        if word.find(letter) == -1:
            return False
    return True
