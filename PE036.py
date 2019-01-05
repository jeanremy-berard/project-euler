def is_palindrome(n):
    n_str = str(n)
    is_palindrome = True
    for i in range(len(n_str)):
        if n_str[i-1] != n_str[-i]:
            is_palindrome = False
    return is_palindrome

sum_binary = 0
for i in range(1000000):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
        sum_binary += i
sum_binary
