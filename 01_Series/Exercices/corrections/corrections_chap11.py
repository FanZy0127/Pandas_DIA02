import pandas as pd
import numpy as np

# # Exercice serie temporelle # #

# 1. Créez une série de dates qui commence en 2019-01-01 (mardi 1 janvier 2019) et qui se termine 30 semaines plus tard,
# associez à chaque date un nombre aléatoire compris entre 100 et 200.

s = pd.Series(
    np.random.randint(100, 200, 30),
    index=pd.date_range('2019-01-01', periods=30, freq='W')
)

print(f'Série : \n{s}')

# 2. Trouvez maintenant les dates pour lesquelles la valeur aléatoire est la plus élevée.
# Même question pour la valeur min.

print(f'Count des valeurs : \n{s.value_counts()}')

# Dates des valeurs max
print(f'Dates des valeurs max : \n{s[s == s.max()]}')
# Dates des valeurs min
print(f'Dates des valeurs min : \n{s[s == s.min()]}')

# Somme des 5 dernières valeurs
print(f'Somme des valeurs des 5 dernières semaines : {s[-5:].sum()}')
