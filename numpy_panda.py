import numpy as np
import pandas as pd

np.array([1, 2, 3])
np.arange(10)
np.arange(9).reshape(3,3)
np.eye(9)
np.random.rand(3,2)
 

mon_array = np.random.rand(5)
my_array_multidim = np.random.rand(6).reshape(3,2)
# print(my_array_multidim[0,])
# print(mon_array)

# print(my_array_multidim.shape)
# print(my_array_multidim.ndim)
# print(my_array_multidim.size)

myarray = np.arange(9).reshape(3, 3)
# print(np.cos(myarray))
# print(np.exp(myarray))
# print(myarray.max(), myarray.min())
# print(np.mean(myarray))

A = np.arange(16).reshape(4,4)
# print(A)
B = np.random.rand(16).reshape(4,4)
# print(B)
# print(A*B)
# print(" ")
# print(A.dot(B))
# print(A.T) #transposé
# print(np.linalg.inv(B))

a = pd.Series(np.array([1,2,3]))
b = pd.DataFrame({"colonne1":[1,2,3],
                  "colonne2":[3,4,5]})

df_covid = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-19-2020.csv')
print(df_covid.head(2))

df_covid.set_index("Confirmed", inplace=True)
print(df_covid.head(2))
df_covid = df_covid.reset_index()
print(df_covid.head(2))
df_covid.rename(columns={"Admin2":"Admin"}, inplace = True)
print(df_covid.head(2))
print(df_covid[df_covid["Country_Region"] == "US"].shape[0] / df_covid.shape[0]*100)

df_covid.columns #récupère toutes les colonnes
print(df_covid[["Province_State", "Active"]])
print(df_covid.set_index("Country_Region").loc["US",["Active","Deaths"]])

df_covid.insert(1, "sum_all_case", df_covid["Active"]+df_covid["Deaths"]+df_covid["Recovered"])
print(df_covid)
df_covid.info()
df_covid.describe()
print(df_covid["Country_Region"].value_counts())

df_covid2 = df_covid.copy()