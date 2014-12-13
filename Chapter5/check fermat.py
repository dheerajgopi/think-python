"""This program helps checking fermats last theorem which states that there
are no positive integers a,b and c, such that
a^n + b^n = c^n
for any values of n greater than 2"""


# defining a function to check fermats theorem

def check_fermat(a,b,c,n):
    ans = (a**n)+(b**n)
                #storing the l.h.s of fermats last theroem to variable "ans"

    if ans == (c**n):
        print "THE ANSWER IS - ",ans
        print "Fermat's last theorem is VALID for the given numbers"
                #checking the validity of fermats last theorem
    else:
        print "THE ANSWER IS - ",ans
        print "Fermat's last theorem is NOT VALID for the given numbers"


print """This program helps checking fermats last theorem which states that there
are no positive integers a,b and c, such that
a^n + b^n = c^n
for any values of n greater than 2"""

# let the user enter any numbers to check the theorems validity

num1 = int(raw_input("Enter any positive integer 'a' :- \n"))
num2 = int(raw_input("Enter any positive integer 'b' :- \n"))
num3 = int(raw_input("Enter any positive integer 'c' :- \n"))
num4 = int(raw_input("Enter any positive integer 'n' :- \n"))

# checking fermats theorem and displaying result
print "a = ",num1
print "b = ",num2
print "c = ",num3
print "n = ",num4
check_fermat(num1,num2,num3,num4)
