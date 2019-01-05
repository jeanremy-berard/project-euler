def sum_digit_power(n,p):
    str_number = str(n)
    sum_digit_power = 0
    for i in range(len(str_number)):
        sum_digit_power += int(str_number[i]) ** p
    return sum_digit_power

i = 9
sum_numbers = 0
while i < 1000000:
    i += 1
    if i == sum_digit_power(i,5):
        sum_numbers += i
sum_numbers
