def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1 : -1]

def is_palindrome(word):
    if len(word)<= 1:   #checking if word length is 1 or less
        return true
    elif first(word)==last(word): # checking if first word = last word
        return True
    else:
        return False
    return is_palindrome(middle(word)) # stripping off first and last characters and recursing the function again
