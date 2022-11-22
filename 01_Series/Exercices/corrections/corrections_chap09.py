import numpy as np
import pandas as pd

# # Exercice méthode groupby # #

fruits = pd.Series(np.random.choice(['banana', 'apple', 'raspberry'], 15))
# Respectivement chaque poids correspond à chaque fruit
# linspace retourne des valeurs espacées équitablement, comprises dans l'intervalle donné (entre 1 et 2),
# et le nombre de fois désiré, ici 15.
weights = pd.Series(np.linspace(1.0, 2.0, 15))

print(f'Fruits : \n{fruits}')
print(f'Weights : \n{weights}')

# 1. Moyenne des poids de chaque fruit
mean_weight_of_each_fruit = weights.groupby(fruits).mean()
print(f'Moyenne des poids de chaque fruit :\n{mean_weight_of_each_fruit}')

# 2. Retournez tous les poids du fruit "banana". Donnez également le nombre de bananes.

# 2.1 Tous les poids du fruit bananes
print(f'Tous les poids des bananes : \n{weights[fruits == "banana"]}')

# 2.2 Nombre de bananes
print(f'Nombre de bananes : {fruits[fruits == "banana"].count()}')

# 3. Ordonnez par somme des poids tous les fruits.
fruits_ordered = weights.groupby(fruits).sum()
print(f'Fruit dont la somme des poids est la plus élevée : \n{fruits_ordered[fruits_ordered == fruits_ordered.max()]}')
print(f'Fruits ordonnés selon la somme de leurs poids : \n{fruits_ordered.sort_values(ascending=False)}')


# # Exercice ville et notes # #

cities = np.random.choice(['Bordeaux', 'Lille', 'Paris'], 100)
notes = np.random.randint(0, 100, 100)

# 1. Créez les deux Séries cities_s et notes_s à partir de ces informations.

cities_s = pd.Series(cities)
print(f'Villes : \n{cities_s}')
notes_s = pd.Series(notes)
print(f'Notes : `\n{notes_s}')

# 2. Donnez la moyenne de chaque ville.

cities_grouped_by_notes = notes_s.groupby(cities_s)
cities_mean = round(cities_grouped_by_notes.mean(), 2)
print(f'Moyenne de chaque ville : \n{cities_mean}')

# 3. Quelle(s) ville(s) a/ont eu la meilleur note des internautes ?
print(f'Ville avec la note la plus haute des internautes : \n{cities_mean[cities_mean == cities_mean.max()]}')

# 4. Y a t il une seule ville qui a eu plus de notes qu'une autre ?
count_notes = notes_s.groupby(cities_s).count()
count_max = count_notes[count_notes == count_notes.max()]
print(f'Nombre de notes de chaque ville : \n{cities_grouped_by_notes.count()}')
print(f'Ville.s avec le plus grand nombre de notes : \n{count_max}')

# 5. On définit maintenant des coefficients pour chacune des notes.
# Calculez la moyenne des notes par ville en considérant ces coefficients.

coeff = np.random.randint(1, 5, 100)

upgraded_notes = pd.Series(notes_s.repeat(coeff))
print(f'Notes avec coefficients : \n{upgraded_notes}')
mean_upgraded_notes = upgraded_notes.groupby(cities_s).mean().sort_values(ascending=False)
print(f'Moyenne des notes avec coefficients : \n{mean_upgraded_notes}')
