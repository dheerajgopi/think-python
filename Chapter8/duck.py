# program for adding string to each letter in 'JKLMNOPQ'

prefix = 'JKLMNOPQ'

for letter in prefix:   
    if letter == 'O' or letter == 'Q':  # adding string 'uack' if 'O' or 'Q'
        print letter + 'uack'
    else:
        print letter + 'ack'
