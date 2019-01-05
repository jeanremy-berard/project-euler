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

i = 9
sum_trunc_prime = 0
while i < 1000000:
    i += 1
    if is_prime(i):
        trunc_prime = True
        for j in range(1,len(str(i))):
            if is_prime(int(str(i)[j:])) == False or is_prime(int(str(i)[:-j])) == False:
                trunc_prime = False
                break
        if trunc_prime == True:
            sum_trunc_prime += i
sum_trunc_prime
