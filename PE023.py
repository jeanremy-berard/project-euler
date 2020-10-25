def is_abundant(n):
    i = 0
    sum_div = 0
    while i+1 <= n/2:
        i += 1
        if n % i == 0:
            sum_div += i
    if sum_div > n:
        return True
    else:
        return False

lst_abundant = list()
for i in range(2,28124):
    if is_abundant(i) == True:
        lst_abundant.append(i)

lst_sum_abundant = list()
for i in range(len(lst_abundant)):
    for j in range(len(lst_abundant)):
        lst_sum_abundant.append(lst_abundant[i] + lst_abundant[j])

non_sum_abundant = 0
for i in range(1,28124):
    if i not in lst_sum_abundant:
        non_sum_abundant += i
non_sum_abundant
