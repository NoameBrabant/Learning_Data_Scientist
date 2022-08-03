import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_poke = pd.read_csv('https://raw.githubusercontent.com/anisayari/Youtube-apprendre-python-intelligence-artificielle/master/%238%20-%20Data%20Visualisation%20(Seaborn%2C%20Plotly)/pokemon.csv')
df_poke.loc[773,"capture_rate"] = 30
df_poke["capture_rate"] = df_poke["capture_rate"].astype(int) 

df_poke.columns = df_poke.columns.str.upper()
print(df_poke.head())     
df_poke["TYPE1"] = df_poke["TYPE1"].str.capitalize  
df_poke["TYPE2"] = df_poke["TYPE2"].str.capitalize
df_poke["TYPE2"].fillna(value = "None", inplace = True)
sns.set(style = "whitegrid")
sns.lineplot( data=df_poke.sort_values(by="DEFENSE"), y="ATTACK", x="DEFENSE")
sns.relplot(x="DEFENSE", y="ATTACK", hue="GENERATION", size="WEIGHT_KG",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=df_poke)
                            
