def printsquare(n):             # Function to print the square of given number n
    print n*n

def do_n(sqre,num):
    if num <= 0:
        return
    else:
        printsquare(num)
        do_n(sqre,num-1)
