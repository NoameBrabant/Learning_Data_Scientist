import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Création des dataframes et time series

df_covid_deaths= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
time_series_France_deaths = df_covid_deaths.iloc[131].drop(['Province/State','Country/Region','Lat','Long'])
df_time_series_France_deaths = pd.DataFrame(time_series_France_deaths).reset_index()
df_covid_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

time_series_France_recovered = df_covid_recovered.iloc[116].drop(['Province/State','Country/Region','Lat','Long'])
df_time_series_France_recovered = pd.DataFrame(time_series_France_recovered).reset_index()
#------------------------------------------------------------- MATPLOTLIB C PAS OUF -------------------------------------------------------------------

#plt.style.use("ggplot")
#time_series_France.plot()
#plt.show()

#------------------------------------SEABORN LE FEU --------------------- PLOTLY AUSSI -----------------------------------------------------------------

df_time_series_France_deaths.columns = ['date', 'death_number']
df_time_series_France_recovered.columns = ["date", "recovered_number"]
df_time_series_France_deaths['date'] = pd.to_datetime(df_time_series_France_deaths["date"])
df_time_series_France_recovered["date"] = pd.to_datetime(df_time_series_France_recovered["date"])
deaths_recovered = { "date" : df_time_series_France_deaths['date'],
                     "deaths" : df_time_series_France_deaths['death_number'],
                     "recovered" : df_time_series_France_recovered["recovered_number"]}

df_deaths_recovered = pd.DataFrame(deaths_recovered)
sns.lineplot(data=df_time_series_France_deaths, x="date", y="death_number")
sns.lineplot(data=df_time_series_France_recovered, x="date", y="recovered_number")
plt.show()


