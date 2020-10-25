def is_pandigital(n):
    is_pandigital = True
    if len(n) != 9:
        is_pandigital = False
    else:
        for i in range(1,10):
            if n.count(str(i)) != 1:
                is_pandigital = False
    return is_pandigital

lst_prod = list()
for i in range(1,10000):
    for j in range(1,10000):
        prod = i * j
        result = str(i) + str(j) + str(prod)
        if is_pandigital(result) == True and prod not in lst_prod:
            lst_prod.append(prod)

sum(lst_prod)
