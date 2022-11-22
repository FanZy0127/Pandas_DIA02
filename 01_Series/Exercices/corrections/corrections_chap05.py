import numpy as np
import pandas as pd

numbers = np.array([12, 6, 8, 19, 10, np.nan, 14, np.nan])
print(numbers.mean())  # affiche nan

numbers = pd.Series([12, 6, 8, 19, 10, np.nan, 14, np.nan])
print(numbers.mean())  # affiche 11.5

print(numbers.isna().sum())  # OU numbers.isnull().sum() affiche la somme des valeurs NaN

# # Exercice remplacer np.nan # #

serie_mean = numbers.mean()  # calcul de la moyenne de la série
nan_mask = numbers.isna()  # masque sur les valeurs NaN de la série
numbers[nan_mask] = serie_mean  # application des moyennes de la série sur les valeurs du masque
print(numbers)
