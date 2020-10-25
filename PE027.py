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

max_prime = 0
prod_coef = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        i = 0
        while is_prime(i * i + a * i + b):
            i += 1
            if i > max_prime:
                max_prime = i
                prod_coef = a * b

prod_coef
