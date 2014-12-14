# approximating the value of pi using the eqn given in exercise

import math

# function for finding factorial
def factorial(n):
    ans = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            ans = ans * i
        return ans

# function for approximating pi
def evaluate_pi():
    const = 2 * math.sqrt(2)/9801
    k = 0
    total = 0

    while True:     # loop for approximating pi until the difference is less than 1e-15
        temp = const*((factorial(4*k))*(1103 + (26390*k)))/(((factorial(k))**4)*(396**(4*k)))
        total = total + temp

        if abs(temp) < 1e-15: # condition for breaking the loop
            break
        k = k+1
    pi = 1/total
    return pi


print evaluate_pi()
