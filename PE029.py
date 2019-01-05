import numpy as np
list_pow = list()
for a in range(2,101):
    for b in range(2,101):
        list_pow.append(a ** b)
        list_pow.append(b ** a)
array_pow = np.array(list_pow)
array_pow_uni = np.unique(array_pow)
len(array_pow_uni)
