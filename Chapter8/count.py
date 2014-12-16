# function for counting the number of times an alphabet appears in a particular string

def count(word,letter,start):
    index = start
    count = 0

    while index < len(word):
        if word[index] == letter:
            count += 1
        index += 1

    print count
