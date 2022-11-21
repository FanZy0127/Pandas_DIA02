# Introduction aux objets Séries de Pandas

## Définition Series

Une série est un tableau indexé à **une seule dimension**, constituée d'un index et de valeur(s) :

```python
data = pd.Series(
    [1000, 7000, 12000 ], # les données
    dtype='int64' # les types
)

# index (numériques)  valeurs
"""
0     1000
1     7000
2    12000
dtype: int64
"""
```

**dtype** indiquera le type de l'objet série, c'est-à-dire le type des données, ici des **int64**.

Sans autre précision pour les indexes, Pandas indexera la série avec un index numérique classique : 0, 1, 2, ...

Vous pouvez cependant préciser les index d'une série directement dans sa définition :

```python
cities = pd.Series(
    [249712, 2190327, 232741 ], # valeur de l'objet Series
    index = ['Bordeaux', 'Paris', 'Lille'] # index personnalisés
)
```

Pour importer Pandas dans un script Python écrivez :

```python
import pandas as pd
```

De manière générale sur une série vous pouvez voir les index et les valeurs à l'aide des deux méthodes suivantes :

```python
s = pd.Series(np.random.randint(0,40, 10))

s.index

s.values

```

Pandas retournera un tableau Numpy pour ces deux méthodes.

Vous pouvez également donner un nom à votre série :

```python
s.name ="Random values"
```

## Les séries sont des objets mutables

Une série est un objet mutable comme les tableaux Numpy, mais à la différence avec ces derniers vous pouvez ajouter des éléments à une série.

```python
ser = pd.Series( np.arange(4, 8), index=['a', 'b', 'c', 'd'] )
ser['e'] = 10

print(ser)
"""
a     4
b     5
c     6
d     7
e    10
"""
```
