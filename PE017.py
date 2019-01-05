pip install num2words

from num2words import num2words

list_num_word = list()
for i in range(1,1001):
    list_num_word.extend(num2words(i).replace('-',' ').split(' '))
total_letters = 0
for i in range(len(list_num_word)):
    total_letters += len(list_num_word[i])
total_letters
