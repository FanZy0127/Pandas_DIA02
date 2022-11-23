import numpy as np
import pandas as pd


# # Exercice Matrice et recherche # #

data = [
    [13, 54, 23, 23, 62, 29, 53, 15, 54, 67],
    [13, 54, 23, 23, 62, 29, 53, 15, 54, 67],
    [98, 36, 34, 40, 13, 92, 41, 61, 94, 62],
    [33, 87, 46, 44, 82, 87, 11, 76, 76, 21],
    [56, 16, 13, 91, 64, 13, 77, 44, 44, 27],
    [56, 16, 13, 91, 64, 13, 77, 44, 44, 27],
    [15, 87, 20, 50, 53, 48, 39, 38, 91, 32],
    [93, 48, 28, 27, 50, 55, 28, 38, 78, 85],
    [76, 58, 26, 89, 88, 71, 97, 80, 42, 52],
    [76, 58, 26, 89, 88, 71, 97, 80, 42, 52],
    [38, 98, 55, 61, 75, 82, 37, 64, 87, 83],
    [24, 53, 16, 84, 82, 13, 18, 18, 82, 51],
]

columns = list("abcdefghij".upper())

matrix_df = pd.DataFrame(data, index=list("abcdefghijkl"), columns=columns)
print(f'Dataframe de la matrice data : \n{matrix_df}')

# 2. Recherchez toutes les lignes identiques dans le DataFrame et supprimez les.
# Vous pouvez utiliser la méthode duplicated sur le DataFrame.

matrix_df = matrix_df[matrix_df.duplicated() == False]

print(f'Dataframe de la matrice après drop des lignes dupliquées : \n{matrix_df}')

# 3. Comptez les occurrences de chaque valeur dans le DataFrame. Placez le résultat de ce comptage dans un dictionnaire.

dictionary = dict()

for index, row in matrix_df.iterrows():
    for c in columns:
        dictionary[row[c]] = matrix_df[matrix_df == row[c]].count().sum()

print(f'Preuve du nombre d\'occurrences de la valeur 13 : {matrix_df[matrix_df == 13].count().sum()}')

print(f'Dictionnaire regroupant les occurrences de chaque valeur du dataframe : \n{dictionary}')

