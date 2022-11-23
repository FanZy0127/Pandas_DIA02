import numpy as np
import pandas as pd


# # Exercices manipulation des index & column # #

df = pd.DataFrame(
    [
        [1, "2", None, 3],
        [4, None, "5", 6],
        [7, 8, 9, 10],
        ["None", "", None, "NAN"],
    ],
    index=['a', 'b', 'c', 'd'],
    columns=['A', 'B', 'C', 'D']
)

df.replace([None, "", "NAN", "None"], np.nan, inplace=True)
print(f'Dataframe : \n{df}')


# # Exercice convertir un array Numpy en DataFrame # #

A = pd.Series(np.random.randint(1, 10, 15))
B = pd.DataFrame(A.values.reshape(3, 5), index=list("abc"), columns=list("defgh"))

print(f'Série A : \n{A}')
print(f'Dataframe : \n{B}')


# # Exercice appliquer une fonction à un DataFrame # #

C = pd.DataFrame(np.random.randn(5, 5), columns=list("abcde"), index=list("fghij"))

C = np.abs(C)
print(f'Dataframe C avec les valeurs absolues : \n{C}')


def amplitude(x):
    return x.max() - x.min()


delta_C_row = C.apply(amplitude, axis=1)
print(f'Amplitude des lignes : \n{delta_C_row}')

delta_C_column = C.apply(amplitude, axis=0)
print(f'Amplitude des colonnes : \n{delta_C_column}')


# # Exercice somme et remplacement # #

D = pd.DataFrame(np.random.randn(5, 5), columns=list("abcde"), index=list("fghij"))


# 1. Faites la somme de toutes les valeurs négatives de D.
print(f'Dataframe avec des valeurs négatives : \n{D}')
neg_mask = D < 0
print(f'Masque des valeurs négatives du Dataframe D : \n{neg_mask}')
sum_neg = D[neg_mask].sum().sum()
print(f'Somme des valeurs négatives du Dataframe D : {sum_neg}')

# 2. Remplacez dans la colonne b les valeurs négatives par la moyenne des valeurs positives de la colonne.

D.loc[D['b'] < 0, 'b'] = D.loc[D['b'] > 0, 'b'].mean()

'''
OU de manière décomposée : 
'''

pos_b = D['b'] >= 0
print(pos_b)
print(len(D[pos_b]))
neg_b = D['b'] < 0
sum_pos_b = D['b'][pos_b].sum()
print(sum_pos_b)
mean_pos_b = sum_pos_b / len(D[pos_b])
print(mean_pos_b)
D[neg_b] = mean_pos_b
print(D)