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