def sum_to_n(n):
    return n * (n+1) / 2

def get_factors(n):
    list_factors = list()
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            list_factors.append(i)
            list_factors.append(int(n/i))
    list_factors = list(set(list_factors))
    return list_factors

i = 1
while len(get_factors(sum_to_n(i))) < 500:
    i += 1
i
