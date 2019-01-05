def reverse_number(n):
    n_str = str(n)
    return int(n_str[::-1])

def is_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        return True
    else:
        return False

def is_lychrel(n):
    step = 0
    while step < 50:
        step += 1
        sum_n_rev = n + reverse_number(n)
        if is_palindrome(sum_n_rev):
            return False
            break
        else:
            n = sum_n_rev
    return True

nb_lychrel = 0
i = 9
while i < 10000:
    i += 1
    if is_lychrel(i):
        nb_lychrel += 1
nb_lychrel
