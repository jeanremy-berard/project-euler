def sum_fact(n):
    from math import factorial
    sum_fact = 0
    str_fact = str(factorial(n))
    for i in range(len(str_fact)):
        sum_fact += int(str_fact[i])
    return sum_fact

sum_fact(100)
