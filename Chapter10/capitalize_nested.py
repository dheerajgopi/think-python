# Function to capitalize the strings in a list

def capitalize_all(t):

    res=[]    # initialising a new list to store the result

    for s in t:
        res.append(s.capitalize())  # appending capitalised strings to the new list
    return res


#Function to capitalised nested list

def capitalize_nested(lst):
    capnest = []
    for i in lst:
        if type(i)==list:
            capnest.append(capitalize_all(i))
        else:
            capnest.append(i.capitalize())
    return capnest
