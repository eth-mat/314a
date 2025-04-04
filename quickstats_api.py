# %% Setup
import requests
import pandas as pd
import numpy as np 
API_KEY = "68628EF2-1FA3-3082-873A-32D62B426347"
BASE_URL = "https://quickstats.nass.usda.gov/api/api_GET/"

 #%%Loading State abbreviations
states = pd.read_csv("states.csv")
state_abbrevs = states[['Abbreviation']]
# %% Creates dfs for each state
for state in state_abbrevs['Abbreviation']:
    params = {
        "key": API_KEY,
        "state_alpha": state,
        "statisticcat_desc": "YIELD",
        "format": "JSON"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            df = pd.DataFrame(data["data"])
            df.to_csv(f"nass_yield_{state}.csv", index=False)
        else:
            print(f"No data returned for {state}")
    else:
        print(f"Error fetching data for {state}: {response.status_code}")

# %%
for state in state_abbrevs['Abbreviation']:
    params = {
    "key": API_KEY,
    "state_alpha": state,
    "statisticcat_desc": "YIELD",
    "format": "JSON",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['data'])
        df.to_csv(f"nass_state_yield_{state}.csv", index=False)
    else:
        print(f"Error: {response.status_code}")
# %%