#### Exercise 10. Is the average of "Valdemorillo" and "Galapagar" price per square meter (price/m2) the same? (★★☆)

#Print the both average prices and then write a conclusion about

#Hint: Create a new column called `pps` (price per square) and then analyse the values

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

#precio medio 
#print(ds['level5'=='Galapagar'])  
ds["pps"] = ds["price"]/ds["surface"] 

# it works ds.loc[(ds['level5'] == "Galapagar")]

print(ds[ds['level5']== "Galapagar"]["pps"].mean())

print(ds[ds['level5']== "Valdemorillo"]["pps"].mean())