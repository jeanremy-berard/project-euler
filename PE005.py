def is_div_20(n):
    is_div_20 = True
    for i in range(2,21):
        if n % i != 0:
            is_div_20 = False
            break
    return is_div_20

n = 1
while is_div_20(n) == False:
    n += 1
n
