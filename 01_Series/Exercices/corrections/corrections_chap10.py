import numpy as np
import pandas as pd

# # Exercice Remplacer et modifier # #

# Soit la chaîne de caractères suivantes :

characters = 'abc def abe dae fab'

# 1. Créez une Séries à partir de characters à l'aide de la méthode list.

s = pd.Series(list(characters))
print(f'Chaîne de caractères transformée en série : \n{s}')

# 2.  Remplacez les espaces (caractères " ") par la valeur np.nan de Numpy.

s[s == ' '] = np.nan
print(f'Série avec des NaN en guise d\'espaces : \n{s}')

# 3. Trouvez la fréquence de la lettre la moins représentée dans la Séries,
# puis remplacez les valeurs NAN par cette lettre.

letters_count = s.value_counts()
print(f'Count de chaque lettre : \n{letters_count}')

least_present_letter = letters_count[letters_count == letters_count.min()]
print(f'Lettre la moins présente : \n{least_present_letter}')

s.fillna(value=least_present_letter.index[0], inplace=True)
print(s)
print("".join(s))
