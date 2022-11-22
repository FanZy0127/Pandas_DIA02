import numpy as np
import pandas as pd


# # Exercice création de DataFrame # #

fruits1 = pd.DataFrame({
    "Raspberry": 30,
    "Cherries": 20
}, index=np.arange(1))

print(fruits1)

fruits2 = pd.DataFrame({
    "fig": [130, 309],
    "wine": [120, 290]
}, index=[2020, 2019])

print(fruits2)


# # Exercices manipulation des index & column # #

df = pd.DataFrame(
    [
        [1, "2", None, 3],
        [4, None, "5", 6],
        [7, 8, 9, 10],
        ["None", "", None, "NAN"],
    ],
    index=['a', 'b', 'c', 'd'],
    columns=['A', 'B', 'C', 'D']
)

df.replace([None, "", "NAN", "None"], np.nan, inplace=True)
print(f'Dataframe : \n{df}')


# # Exercice convertir un array Numpy en DataFrame # #

A = pd.Series(np.random.randint(1, 10, 15))
B = pd.DataFrame(A.values.reshape(3, 5), index=list("abc"), columns=list("defgh"))

print(f'Série A : \n{A}')
print(f'Dataframe : \n{B}')
