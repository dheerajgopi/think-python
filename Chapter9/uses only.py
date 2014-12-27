def uses_only(word,alphabets):
    for letter in word:
        if alphabets.find(letter) == -1:
            return False
    return True
