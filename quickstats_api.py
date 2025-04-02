# %% Setup
import requests
import pandas as pd
import numpy as np 
API_KEY = "68628EF2-1FA3-3082-873A-32D62B426347"
BASE_URL = "https://quickstats.nass.usda.gov/api/api_GET/"

#%% Setting params
params = {
    "key": API_KEY,
    "commodity_desc": "CORN",
    "state_alpha": "IA",
    "statisticcat_desc": "YIELD",
    "format": "JSON",
}

#%% Response
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data['data'])
    print(df.head())

    df.to_csv("nass_corn_yield_IA.csv", index=False)
else:
    print(f"Error: {response.status_code}")



# %%
df = pd.read_csv("nass_corn_yield_IA.csv")
print(df.describe())

df.drop(['asd_code', 'watershed_desc', 'week_ending', 'state_fips_code', 'county_code', 'state_name', 'county_name', 'statisticcat_desc'], axis=1, inplace=True)
# %%
df.head()
# %%
