# function to check whether the given two strings are anagrams

def is_anagram(word1,word2):

    if len(word1)!=len(word2): 	# if words are of different length return false
        return False

    else:			# if words are of same length convert the string into lists and sort them in ascending order

        word_a=list(word1)
        word_a.sort()
        word_b=list(word2)
        word_b.sort()

        if word_a == word_b:	# if lists are equal return true....else false
            return True
        else:
            return False
