import math

def factorial(n):
    ans = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            ans = ans * i
        return ans

def evaluate_pi():
    const = 2 * math.sqrt(2)/9801
    k = 0
    total = 0
    while True:
        temp = const*((factorial(4*k))*(1103 + (26390*k)))/(((factorial(k))**4)*(396**(4*k)))
        total = total + temp

        if abs(temp) < 1e-15:
            break
        k = k+1
    pi = 1/total
    return pi


print evaluate_pi()
