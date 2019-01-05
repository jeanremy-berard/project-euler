prev_val = 1
grid = 1001
sum_diag = 1
for i in range(1,grid * 2 - 1):
    new_val = prev_val + ((i-1) // 4 + 1) * 2
    sum_diag += new_val
    prev_val = new_val
sum_diag
