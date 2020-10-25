def is_prime(n):
    is_prime = True
    if n == 2:
        is_prime = True
    elif n % 2 == 0:
        is_prime = False
    elif n > 1:
        is_prime = True
        for i in range(3,int(n**0.5)+1,2):
            if n % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    return is_prime

def is_pandigital_n(i,n):
    pandigital = True
    if len(str(i)) != n:
        pandigital = False
    else:
        for j in range(1,n+1):
            if str(i).count(str(j)) != 1:
                pandigital = False
    return pandigital

max_prime_pandigital = 0
for i in range(1,1000000000):
    l = len(str(i))
    if is_pandigital_n(i,l) == True:
        if is_prime(i) == True:
            max_prime_pandigital = i

max_prime_pandigital
