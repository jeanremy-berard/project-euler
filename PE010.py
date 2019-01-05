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

sum_prime = 0
for i in range(2000000):
    if is_prime(i):
        sum_prime += i
sum_prime
