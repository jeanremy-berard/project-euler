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

def all_rotations(n):
    rotation = str(n)
    lst_rotations = [rotation]
    for i in range(1,len(rotation)):
        rotation = rotation[1:] + rotation[0]
        lst_rotations.append(rotation)
    return lst_rotations

circ_prime = 0
for i in range(1,1000000):
    all_prime = True
    for j in all_rotations(i):
        if is_prime(int(j)) == False:
            all_prime = False
    if all_prime == True:
        circ_prime += 1

circ_prime
