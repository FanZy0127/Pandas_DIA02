import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# On récupère uniquement le dataset iris
from sklearn.datasets import load_iris

# C'est un dictionnaire
iris = load_iris()

# Les clés du dictionnaire
iris.keys()

# Nous allons essayer de visualiser une corrélation entre la longueur et
# la largeur des sépales des trois espèces d'iris.
# Utilisez un DataFrame Pandas pour faire cette représentation graphique.

iris_names = pd.Series(iris['target_names'])
print(f'Noms des différentes espèces d\'iris : \n{iris_names}\n')
feature_names = iris['feature_names']
print(f'Noms des colonnes : \n{feature_names}\n')

df = pd.DataFrame(data=iris.data, columns=feature_names, index=iris_names[iris.target])
print(df.head())

sns.scatterplot(data=df, x="sepal length (cm)", y="sepal width (cm)", hue=df.index)
plt.title('Corrélation entre longueur/largeur des sépales des iris.')
plt.show()

sns.regplot(data=df[df.index == "setosa"], x="sepal length (cm)", y="sepal width (cm)", robust=True, ci=None)
plt.title('Droite de régression linéaire des sépales des iris Setosa.')
plt.show()

sns.regplot(data=df[df.index == "versicolor"], x="sepal length (cm)", y="sepal width (cm)", robust=True, ci=None)
plt.title('Droite de régression linéaire des sépales des iris Versicolor.')
plt.show()

sns.regplot(data=df[df.index == "virginica"], x="sepal length (cm)", y="sepal width (cm)", robust=True, ci=None)
plt.title('Droite de régression linéaire des sépales des iris Virginica.')
plt.show()

df_setosa_sepals = pd.DataFrame(
    {'x': df[df.index == "setosa"]["sepal length (cm)"], 'y': df[df.index == "setosa"]["sepal width (cm)"]}
)
df_versicolor_sepals = pd.DataFrame(
    {'x': df[df.index == "versicolor"]["sepal length (cm)"], 'y': df[df.index == "versicolor"]["sepal width (cm)"]}
)
df_virginica_sepals = pd.DataFrame(
    {'x': df[df.index == "virginica"]["sepal length (cm)"], 'y': df[df.index == "virginica"]["sepal width (cm)"]}
)

print(f'Coefficients de corrélation des sépales des iris Setosa : \n{df_setosa_sepals.corr(method="pearson")}\n')
print(f'Coefficients de corrélation des sépales des iris Versicolor : \n{df_versicolor_sepals.corr(method="pearson")}\n')
print(f'Coefficients de corrélation des sépales des iris Virginica : \n{df_virginica_sepals.corr(method="pearson")}\n')

"D'après l'interprétation des graphiques ci-dessus, et grâce aux calculs des différents coefficients de corrélation, " \
"nous pouvons conclure que pour les Setosas, la longueur des sépales est très corrélée à leur largeur. "
"En revanche pour ce qui est des Versicolors, la longueur et la largeur des sépales sont moyennement corrélées. Et " \
"elles sont encore moins corrélées pour les Virginicas. "

# Vous ferez un deuxième graphique par rapport aux pétales pour voir
# s'il y a également une corrélation.

sns.scatterplot(data=df, x="petal length (cm)", y="petal width (cm)", hue=df.index)
plt.title('Corrélation entre longueur/largeur des pétales des iris.')
plt.show()

sns.regplot(data=df[df.index == "setosa"], x="petal length (cm)", y="petal width (cm)", robust=True, ci=None)
plt.title('Droite de régression linéaire des pétales des iris Setosa.')
plt.show()

sns.regplot(data=df[df.index == "versicolor"], x="petal length (cm)", y="petal width (cm)", robust=True, ci=None)
plt.title('Droite de régression linéaire des pétales des iris Versicolor.')
plt.show()

sns.regplot(data=df[df.index == "virginica"], x="petal length (cm)", y="petal width (cm)", robust=True, ci=None)
plt.title('Droite de régression linéaire des pétales des iris Virginica.')
plt.show()

df_setosa_petals = pd.DataFrame(
    {'x': df[df.index == "setosa"]["petal length (cm)"], 'y': df[df.index == "setosa"]["petal width (cm)"]})
df_versicolor_petals = pd.DataFrame(
    {'x': df[df.index == "versicolor"]["petal length (cm)"], 'y': df[df.index == "versicolor"]["petal width (cm)"]})
df_virginica_petals = pd.DataFrame(
    {'x': df[df.index == "virginica"]["petal length (cm)"], 'y': df[df.index == "virginica"]["petal width (cm)"]})

print(f'Coefficients de corrélation des pétales des iris Setosa : \n{df_setosa_petals.corr(method="pearson")}\n')
print(f'Coefficients de corrélation des pétales des iris Versicolor : \n{df_versicolor_petals.corr(method="pearson")}\n')
print(f'Coefficients de corrélation des pétales des iris Virginica : \n{df_virginica_petals.corr(method="pearson")}\n')

"D'après l'interprétation des graphiques ci-dessus, et grâce aux calculs des différents coefficients de corrélation, " \
"nous pouvons conclure que pour les Versicolors, la longueur des pétales est très corrélée à leur largeur. "
"En revanche pour ce qui est des Setosas, la longueur et la largeur des sépales sont faiblement corrélées. Et elles " \
"sont également peu corréléees pour les Virginicas. "


# Diagramme à moustache
# Diagramme pour les sepal

plt.subplot(121)
plt.boxplot(df_setosa_sepals['x'], positions=[1], widths=0.6)
plt.boxplot(df_versicolor_sepals['x'], positions=[2], widths=0.6)
plt.boxplot(df_virginica_sepals['x'], positions=[3], widths=0.6)

plt.gca().xaxis.set_ticklabels(['Setosa', 'Versicolor', 'Virginica'])
plt.title("Sepal length (cm)")

plt.subplot(122)
plt.boxplot(df_setosa_sepals['y'], positions=[1], widths=0.6)
plt.boxplot(df_versicolor_sepals['y'], positions=[2], widths=0.6)
plt.boxplot(df_virginica_sepals['y'], positions=[3], widths=0.6)

plt.gca().xaxis.set_ticklabels(['Setosa', 'Versicolor', 'Virginica'])
plt.title("sepal width (cm)")

plt.show()

# Diagramme pour les petales

plt.subplot(121)
plt.boxplot(df_setosa_petals['x'], positions=[1], widths=0.6)
plt.boxplot(df_versicolor_petals['x'], positions=[2], widths=0.6)
plt.boxplot(df_virginica_petals['x'], positions=[3], widths=0.6)

plt.gca().xaxis.set_ticklabels(['Setosa', 'Versicolor', 'Virginica'])
plt.title("petal length (cm)")

plt.subplot(122)
plt.boxplot(df_setosa_petals['y'], positions=[1], widths=0.6)
plt.boxplot(df_versicolor_petals['y'], positions=[2], widths=0.6)
plt.boxplot(df_virginica_petals['y'], positions=[3], widths=0.6)

plt.gca().xaxis.set_ticklabels(['Setosa', 'Versicolor', 'Virginica'])
plt.title("petal width (cm)")

plt.show()
