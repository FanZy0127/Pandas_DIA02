import numpy as np
import pandas as pd

# Exercice création d'objet "Séries" avec un dictionnaire Python

cities = pd.Series({
    'Bordeaux': 249712,
    'Paris': 2190327,
    'Lille': 232741
})

print(cities)
print(cities.Paris)
print(cities["Paris"])

# Exercice construire des objets de type Séries

values = range(1, 12, 2)
index = 'abcdef'

A = pd.Series(values, index=list(index))

print(A)

# Exercice changez les index

cities = {
    'Bordeaux': 249712,
    'Paris': 2190327,
    'Lille': 232741
}

cities_serie = pd.Series(cities)
print(cities_serie)

# Bordeaux : 33, Paris : 75, Lille : 59
departements = [33, 75, 59]
cities_serie.index = departements
print(cities_serie)

mask = cities_serie.values > 2000000
print(f'Villes dont la population est supérieure à 2 000 000 : {cities_serie[mask]}.')

# Augmentation de 10%
cities_serie = cities_serie * 1.1
print(cities_serie)
