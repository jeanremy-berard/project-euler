def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        sum_number = sum_digits(a**b)
        if sum_number > max_sum:
            max_sum = sum_number

max_sum
