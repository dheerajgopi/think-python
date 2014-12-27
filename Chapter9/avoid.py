def avoids(word,forbidden):
    for letter in forbidden:
        if word.find(letter) != -1:
            return False
    return True
