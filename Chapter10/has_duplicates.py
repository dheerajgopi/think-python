# checks if there are duplicates in the list WITHOUT MODIFYING THE LIST

def has_duplicates(lst):

    for i in range(0,len(lst)):    # nested for loop for comparing each element with rest of the elements

        for j in range(i+1,len(lst)):

            if lst[i]==lst[j]:     # returns true if duplicate is found
                return True
    
    return False                   # else returns false
