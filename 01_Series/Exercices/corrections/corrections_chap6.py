import numpy as np
import pandas as pd

# # Exercice notes et effectifs # #

notes = pd.Series([1, 7, 8, 9, 10, 12, 15, 17, 18, 19, 20])
effectifs = pd.Series([2, 3, 2, 1, 5, 7, 2, 6, 2, 1, 1])

# 1. Quel est le pourcentage d'étudiants de la promo Data01 ayant obtenu une note comprise entre 9 et 13 ?
percentage_grades_between_9_and_13 = round(effectifs[(notes > 8) & (notes < 14)].sum() / effectifs.sum(), 2) * 100
print(f'Il y a {percentage_grades_between_9_and_13}% des étudiants qui ont eu entre 9 et 13.')

# 2. Combien d'étudiants ont obtenu une note inférieur à 10 strictement.
grades_lower_than_10 = effectifs[notes < 10].sum()
print(f'{grades_lower_than_10} étudiants ont obtenu une note strictement inférieure à 10.')

# 3. Déterminez la moyenne de la promo.

mean_promo = (effectifs * notes).sum() / effectifs.sum()
print(f'La moyenne de la promo est de {round(mean_promo, 2)}.')

# 4. Déterminez la note médiane.

Notes = np.repeat(notes, effectifs)

print(Notes.describe())

median = Notes.median()  # ou Notes.describe()['50%']
q1 = Notes.describe()['25%']
q3 = Notes.describe()['75%']

print(f'Quartile 1 : {q1}, Médiane : {median}, Quartile 3 : {q3}')
