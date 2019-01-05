def get_factors_wo_n(n):
    list_factors = [1]
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            list_factors.append(i)
            list_factors.append(int(n/i))
    list_factors = list(set(list_factors))
    return list_factors

list_amicable = list()
for i in range(10000):
    if i not in list_amicable:
        sum_factors = sum(get_factors_wo_n(i))
        if sum(get_factors_wo_n(sum_factors)) == i and i != sum_factors:
            list_amicable.append(i)
            list_amicable.append(sum_factors)
sum(list_amicable)
