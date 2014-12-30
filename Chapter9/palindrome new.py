def palindrome(word,first,last):
    if word[first:last+1] == word[last:first-1:-1]:
        return True
    else:
        return False
