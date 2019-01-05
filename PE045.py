def get_triangle_numbers(n):
    list_tri_numbers = list()
    for i in range(n):
        list_tri_numbers.append(int((i+1) * (i+2) / 2))
    return list_tri_numbers

def is_pentagonal(n):
    k = ((24*n + 1) ** 0.5 + 1) / 6
    if k - int(k) > 0:
        return False
    else:
        return k

def is_hexagonal(n):
    k = ((8*n + 1) ** 0.5 + 1) / 4
    if k - int(k) > 0:
        return False
    else:
        return k

list_tri = get_triangle_numbers(100000)
list_tri = [i for i in list_tri if i > 40755]

i = 40755
for i in list_tri:
    if is_pentagonal(i) != False:
        if is_hexagonal(i) != False:
            break
i
