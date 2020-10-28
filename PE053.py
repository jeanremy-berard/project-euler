import math

comb_over_million = 0
for n in range(1,101):
    for r in range(1,n+1):
        comb = math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
        if comb >= 1000000:
            comb_over_million += 1

comb_over_million
