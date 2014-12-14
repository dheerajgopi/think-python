# function for returning the factorial of the given number

def factorial(n):

    ans = 1         # initialising a variable with 1
            
    if n == 0:      # checking if given value is 0
        return 1

    else:
        for i in range(1,n+1):  # incrementing i value until n and multiplying
            ans = ans * i
            print ans
        return ans
