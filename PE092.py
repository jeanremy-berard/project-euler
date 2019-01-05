def square_digits(n):
    n_str = str(n)
    square_digits = 0
    for i in range(len(n_str)):
        square_digits += int(n_str[i]) ** 2
    return square_digits

def number_chain(n):
    while n != 89 and n != 1:
        n = square_digits(n)
    return n

nb_89 = 0
for i in range(1,10000000):
    if number_chain(i) == 89:
        nb_89 += 1
nb_89
