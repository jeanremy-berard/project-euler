import pandas as pd

def score_word(word):
    score = 0
    for i in range(len(word)):
        score += ord(word[i]) - 64
    return score

with open('PE022_names.txt') as f:
    str_names = f.readlines()
str_names = str_names[0].replace('"','')
list_names = str_names.split(',')
df_names = pd.DataFrame(list_names,columns=['FirstName']).sort_values('FirstName')
df_names['LengthFN'] = df_names['FirstName'].apply(lambda x:score_word(x))
df_names['Rank'] = df_names['FirstName'].rank(ascending=True)
df_names['Score'] = df_names['LengthFN'] * df_names['Rank']
df_names['Score'].sum()
