import itertools
def get_permutations(n):
    n_str = str(n)
    list_perm = list()
    for perm in itertools.permutations(n_str,len(n_str)):
        list_perm.append(perm)
    for i in range(len(list_perm)):
        perm = ''
        for j in range(len(n_str)):
            perm += list_perm[i][j]
        list_perm[i] = int(perm)
    return list_perm

perm_0to9 = get_permutations('0123456789')
perm_0to9[999999]
