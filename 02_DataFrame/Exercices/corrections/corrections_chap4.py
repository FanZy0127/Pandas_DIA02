import pandas as pd
import numpy as np


# # Exercice de regroupement par pays # #

dataset = {
    'name': ['john', 'mary', 'peter', 'jeff', 'bill', 'lisa', 'jose'],
    'age': [23, 78, 22, 19, 45, 33, 20],
    'gender': ['M', 'F', 'M', 'M', 'M', 'F', 'M'],
    'city': ['Paris', 'Lille', 'Paris', 'Lille', 'Paris', 'Bordeaux', 'Bordeaux'],
    'num_children': [3, 0, 2, 4, 3, 1, 5],
    'num_pet': [5, 1, 0, 5, 2, 2, 3],
    'status': ['married', 'married', 'married', 'divorced', 'divorced', 'married', 'married']
}

# 1. Reprenez le dataset suivant et donnez le nombre d'enfant(s) par ville dans un tableau
# à deux colonnes city & num_children.

df = pd.DataFrame(dataset)
print(f'Dataframe : \n{df}')
dfg = df.groupby('city')[['city', 'num_children']].sum()
print(f'Dataframe groupé par ville et nombre d\'enfants : \n{dfg}')

# 2. Quel est l'écart des âges des habitants par ville ?

print(f'Amplitude des âges des habitants par ville : \n'
      f'{df.groupby("city")[["age"]].apply(lambda x: x.max() - x.min())}')

# 3. Est-ce que les femmes mariées ont plus d'enfant que les hommes divorcés ?

dff = df[(df['status'] == 'married') & (df['gender'] == 'F')]['num_children'].sum()
dfm = df[(df['status'] == 'divorced') & (df['gender'] == 'M')]['num_children'].sum()

print(f'Somme des enfants des femmes mariées : {dff}')

print(f'Somme des enfants des hommes divorcés : {dfm}')

print("Les femmes mariées ont plus d\'enfants que les hommes divorcés." if dff > dfm else
      "Les femmes mariées ont moins d\'enfants que les hommes divorcés.")

# 4. Quelle est la ville où les femmes ont le plus de chiens ? Même question pour les hommes ?

city_num_pet_f = df[df['gender'] == 'F'].groupby('city')['num_pet'].sum().idxmax()

print(f'La ville où les femmes ont le plus de chiens est {city_num_pet_f}.')

city_num_pet_m = df[df['gender'] == 'M'].groupby('city')['num_pet'].sum().idxmax()

print(f'La ville où les hommes ont le plus de chiens est {city_num_pet_m}.')


# # Exercice pourboires # #

tips = pd.read_csv('../data/tips.csv')
print(f'Dataframe tips head (5 premières lignes) : \n{tips.head()}')

# 1. Ajoutez une colonne ['tips_perct'] au DataFrame tips,
# elle calculera le pourcentage de chaque pourboire par rapport au total des pourboires.

tips['tips_perct'] = np.round(tips['tip'] / tips['total_bill'] * 100, 2)

print(f'Dataframe tips head (5 premières lignes) après ajout de la colonne tips_perct : \n{tips.head()}')

# 2. Quels sont les pourcentages des pourboires par rapport au sexe et à la consommation de tabac ?
# Donnez leurs moyennes et écarts types.

print(f'Pourcentages des pourboires par rapport au sexe et à la consommation de tabac : \n'
      f'{round(tips.groupby(["sex", "smoker"])["tips_perct"].agg(["mean", "std"]), 2)}')

# 3. Calculez l'étendue des pourboires pour les femmes qu'elles fument ou ne fument pas. Créez une fonction
# peak_to_peak et appliquez cette fonction, comme une fonction d'agrégation,
# à votre groupement à l'aide de la fonction agg de Pandas.


def peak_to_peak(array):
    return array.max() - array.min()


extend_female_tips = tips[tips['sex'] == 'Female'].groupby('smoker')['tip'].agg(peak_to_peak)
print(f'Étendue des pourboires des femmes selon le fait qu\'elles fument ou non : \n{extend_female_tips}')

# 4. En utilisant le même regroupement par sex et smoker et en utilisant la fonction agg de Pandas, calculez le max
# des pourboires ainsi que le nombre. Vous pouvez passer à la méthode agg un dictionnaire pour spécifier les fonctions
# à appliquer par colonne.

print(f'Regroupemeent des pourboires maximum et du nombre de pourboires, par sex et smoker : \n'
      f'{tips.groupby(["sex", "smoker"]).tip.agg(["max", "count"])}')
print(f'Avec avec un dictionnaire en paramètre de la fonction agg : \n'
      f'{tips.groupby(["sex", "smoker"]).agg({"tip": np.max, "size": np.sum})}')


# # Exercice grouper avec un dictionnaire # #

# 1. Créez le DataFrame population avec les données ci-après.

data = [
    [1.00337786,  1.60212136,  0.4597855,  0.50281771,  0.65316509],
    [-0.57524468, -0.19829894,  0.05230613, -0.03159951, -0.42909259],
    [0.54683457,  1.85576317, -0.62295055, -1.43870874, -0.4367706],
    [1.18701531,  0.59918783,  0.78498521,  1.25839299, -0.97814535],
    [0.51031798, -2.35260978, -1.87559638, -0.23625731,  2.14360896]
]

population = pd.DataFrame(data,
                          columns=list("abcde"),
                          index=["Alan", "Bernard", "Sophie", "Noe", "Alice"])

print(f'DataFrame population : \n{population}')

# 2. Créez un dictionnaire mapping, les clés sont les noms des colonnes et les valeurs les noms des relations.
# Puis appliquez ce mapping à votre regroupement sur les colonnes. Faites la somme de ces valeurs.

mapping = {'a': 'first', 'b': 'first', 'c': 'second', 'd': 'second', 'e': 'second'}

grouped = population.T.groupby(mapping).sum().T

'''
OU

grouped = population.groupby(mapping).sum(axis=1)

OU ENCORE

grouped = population.T.groupby(mapping).sum()
'''

print(f'DataFrame grouped : \n{grouped}')
