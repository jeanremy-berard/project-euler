def collatz(n):
    step = 1
    while n > 1:
        step += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3+1
    return step

longest_chain = 0
start_nb = 0
i = 0
while i < 1000000:
    i += 1
    new_chain = collatz(i)
    if new_chain > longest_chain:
        longest_chain = new_chain
        start_nb = i
longest_chain, start_nb
