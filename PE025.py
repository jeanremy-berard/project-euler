def fibonacci_list(n):
    fibo_list = list()
    if n == 1:
        fibo_list = [1]
    else:
        i = 2
        fibo_list = [1,1]
        while i < n:
            i += 1
            fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list

n = 1
while len(str(fibonacci_list(n)[-1])) < 1000:
    n += 1
n
