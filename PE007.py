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

nb_prime = 0
n = 1
while nb_prime < 10001:
    n += 1
    if is_prime(n):
        nb_prime += 1
n
