#Factorial of a number 

def fact(num):
    if num ==0:
        return 1
    else:
        return num * fact(num - 1)

n = 5
f = fact(n)
print("factorial of the " ,n, " is : ",f)