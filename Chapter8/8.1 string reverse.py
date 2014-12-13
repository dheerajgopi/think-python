def string_reversal(word):
    if not isinstance(word, str):
        print "Please enter a string value"
    else:
        index = len(word)-1
        while index>=0:
            print word[index]
            index -= 1
