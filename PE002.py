def fibonacci(n):
    if n > 2:
        fibo = fibonacci(n-2) + fibonacci(n-1)
    elif n == 2:
        fibo = 2
    else:
        fibo = 1
    return fibo

sum = 0
for i in range(50):
    if fibonacci(i) > 4000000:
        break
    else:
        if fibonacci(i) % 2 == 0:
            sum += fibonacci(i)
sum
