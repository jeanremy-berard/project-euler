def is_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        return True
    else:
        return False

sum_binary = 0
for i in range(1000000):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
        sum_binary += i
sum_binary
