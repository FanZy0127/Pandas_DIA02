import pandas as pd

# # Exercice Séries A & B # #

A = pd.Series([1, 21, 13, 14, 59])
B = pd.Series([14, 21, 3, 4, 5, 1])

# 1. Soit les deux Séries A et B suivantes, récupérez les valeurs de la série A
# qui ne sont pas présentes dans la série B.

mask = A.isin(B)
print(f'Masque des valeurs de A non-présentes dans B : \n{mask}')
print(f'Valeurs de A non-présentes dans B : \n{A[~mask]}')

# 2.Donnez les valeurs de l'intersection de A et B.

print(f'Valeurs e l\'intersection de A et B : \n{A[mask]}')

# 3. Quelles sont toutes les valeurs de A qui ne sont pas dans B et toutes les valeurs de B qui ne sont pas dans A.

dataset = pd.concat([B[~B.isin(A)], A[~mask]], ignore_index=True)

print(f'Dataset de toutes les valeurs de A non-présentes dans B et de toutes les valeurs de B non-présentes dans A :\n'
      f'{dataset}')
