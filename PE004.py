def is_palindrome(n):
    n_str = str(n)
    is_palindrome = True
    for i in range(len(n_str)):
        if n_str[i-1] != n_str[-i]:
            is_palindrome = False
    return is_palindrome

list_palindrome = list()
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i * j) == True:
            list_palindrome.append(i * j)
max(list_palindrome)
