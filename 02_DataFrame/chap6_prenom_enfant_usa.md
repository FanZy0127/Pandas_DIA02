# Prénoms des enfants aux Etats-Unis

Pour les besoins de l'étude qui suit importez les dépendances suivantes :

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## Présentation & organisation

L'administration américaine de la sécurité sociale (USSSA ou SSA) a rendu publique les données sur la fréquence des prénoms attribués aux bébés depuis 1880 jusqu'en 2018.

Récupérez les sources names.zip à l'adresse suivante : [baby](https://www.ssa.gov/oact/babynames/limits.html), puis dézippez celle-ci dans un dossier data à la racine de vos notebook.

1. Récupérez le fichier yob1880.txt et créez un DataFrame names_1880 à partir de ces données. Pour charger ce DataFrame vous utiliserez la méthode **read_csv** de Pandas. Renommez les colonnes avec l'argument **names** de cette méthode avec respectivement les noms suivants  : "name", "sex" et "birth".

2. Donnez le nombre de naissances par sexe pour l'année 1880.

## Création du DataFrame names

3. Créez un script permettant de récupérer les prénons de 1880 à 2018 à partir des fichiers du dossier names et utiliser la méthode concat pour les rassembler. Utilisez la méthode concat de Pandas, vous pouvez également pour plus cohérence au niveau des index dans l'agrégation des données, ignorer les index de chaque DataFrame, avec le paramètre ignore_index = True dans la méthode concat. Dans ce cas les index seront 0 ... n-1 dans le DataFrame agrégé.

## Création du DataFrame total_births

4. Agrégez les données pour avoir deux colonnes F et M. Et faites la somme des naissances par sexe et par année. Vous pouvez utiliser la méthode pivot_table.

Vous pouvez également comparer avec un groupby pour la représentation des données. Notez que par la suite nous utiliserons un groupby sur notre DataFrame de l'ensemble des prénoms.

```python
# Fonction Pandas reportez vous à la documentation 
pivot_table()
```
![pivot](images/pivot.png)

5. Représentez graphiquement le total des naissances par sexe et par année. Appliquez ce qui suit pour vérifier la cohérence de vos données.

Indications :

```python
total_births.plot(title="Total des Naissance par sex et par an")
plt.xlabel("Year")
plt.legend(title="Sex");
```

## Retour au DataFrame names

6. Ajoutez une colonne prop au DataFrame, elle représentera le nombre d'enfants ayant reçu un prénom par rapport au nombre total de naissances : une valeur de 0.02 par exemple indiquera que 2 enfants sur 100 ont reçu un prénom donné. On regroupera ainsi les données par sexe et âge en ajoutant la colonne prop.

*Indications : utilisez une fonction appliquée aux groupements comme suit sur. Vous pouvez pour également passer une fonction à la place du lambda. Ce regroupement appliqué créera un groupement supplémentaire par proportion de prénom pour chaque année.*

```python
groupDataFrame.apply(myFunc)
def myFunc(group):
    pass
```

7. Vérifiez maintenant que pour tous les groupes la somme des proportions est bien égale à 1. Utilisez la méthode **np.allclose** de Numpy.

8. Extrayez maintenant des sous-ensembles de 1000 prénoms par groupe de sexe et d'année. Créez une fonction get_top1000 qui les calculera.

9. Affichez, les prénoms par ordre décroissant de naissance pour l'année 1880. Et trouvez pour cette année le prénom le plus populaire quel que soit le sexe.

Dans la suite on travaillera avec ces sous-ensembles.

10. Etudiez maintenant la tendance des prénoms suivants : John, Harry, Mary, Marilyn ; faites un graphique voyez ci-dessous. Créez une table de pivot du nombre total de naissances par an et par prénom.

```python
# Si total_births_top1000 est votre DataFrame pour représenter les différentes colonnes
total_births_top1000.plot(subplots=True, figsize=(12,10), grid=False, title="Nombre de naissance par an")
```

11. Essayez maintenant de mesurer la diversité des prénoms. Donnez une explication en fonction des résultats de cette tendance qui vous semble correspondre aux graphiques. Étudiez les proportions de prénoms dans les Top1000.
