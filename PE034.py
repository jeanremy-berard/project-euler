import math

def nb_equals_fact(n):
    import math
    str_nb = str(n)
    sum_fact = 0
    for i in range(len(str_nb)):
        sum_fact += math.factorial(int(str_nb[i]))
    return sum_fact == n

sum_nb_fact = 0
for i in range(10,1000000):
    if nb_equals_fact(i) == True:
        sum_nb_fact += i
sum_nb_fact
