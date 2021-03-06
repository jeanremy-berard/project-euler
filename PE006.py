def sum_of_square(n):
    sum = 0
    for i in range(n + 1):
        sum += i ** 2
    return sum

def square_of_sum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum ** 2

def diff(n):
    return square_of_sum(n) - sum_of_square(n)

diff(100)
