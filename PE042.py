def score_word(word):
    score = 0
    for i in range(len(word)):
        score += ord(word[i]) - 64
    return score

def get_triangle_numbers(n):
    list_tri_numbers = list()
    for i in range(n):
        list_tri_numbers.append(int((i+1) * (i+2) / 2))
    return list_tri_numbers

tri_numbers = get_triangle_numbers(100)

with open('PE042_words.txt') as f:
    str_words = f.readlines()
str_words = str_words[0].replace('"','')
list_words = str_words.split(',')

nb_tri_words = 0
for word in list_words:
    if score_word(word) in tri_numbers:
        nb_tri_words += 1
nb_tri_words
