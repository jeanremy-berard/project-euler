def is_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        return True
    else:
        return False

list_palindrome = list()
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i * j) == True:
            list_palindrome.append(i * j)
max(list_palindrome)
