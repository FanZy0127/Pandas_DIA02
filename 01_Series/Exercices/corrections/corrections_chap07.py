import pandas as pd

# # Exercice apply # #

serie = pd.Series([
    'adaline Reichel',
    'dr. Santa Prosacco DVM',
    'noemy Vandervort V',
    'lexi O Conner',
    'gracie Weber',
    'roscoe Johns',
    'emmett Lebsack',
    'keegan Thiel',
    'wellington Koelpin II',
    'ms. Karley Kiehn V',
])

first_names = serie.apply(lambda x: x[0].upper() + x[1:])
print(first_names)
