def factorial(n):
    ans = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            ans = ans * i
            print ans
        return ans
