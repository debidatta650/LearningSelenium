#To find prime numbers between 1-10
def prime_num(n):
    if n < 2:
        return False
        
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
a = 1
b = 10

for nu in range (a, b+1):
    if prime_num(nu):
        print (nu)

    