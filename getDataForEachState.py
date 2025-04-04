# %% Setup
import requests
import pandas as pd
import numpy as np 
API_KEY = "68628EF2-1FA3-3082-873A-32D62B426347"
BASE_URL = "https://quickstats.nass.usda.gov/api/api_GET/"


# %%
state2abbrev = {
        'Alaska': 'AK',
        'Alabama': 'AL',
        'Arkansas': 'AR',
        'Arizona': 'AZ',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'District of Columbia': 'DC',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Iowa': 'IA',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Massachusetts': 'MA',
        'Maryland': 'MD',
        'Maine': 'ME',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Missouri': 'MO',
        'Mississippi': 'MS',
        'Montana': 'MT',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Nebraska': 'NE',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'Nevada': 'NV',
        'New York': 'NY',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Virginia': 'VA',
        'Vermont': 'VT',
        'Washington': 'WA',
        'Wisconsin': 'WI',
        'West Virginia': 'WV',
        'Wyoming': 'WY',
        'Puerto Rico': 'PR',
        'Virigin Islands': 'VI'
    }
def perStateData(the_list):
    
    for state in the_list:
        params = {
    "key": API_KEY,
    "commodity_desc": "CORN",
    "state_alpha": state,
    "statisticcat_desc": "YIELD",
    "format": "JSON",
        }
    response = requests.get(BASE_URL, params=params)
    file_name = "nass_corn_yield_" + state + ".csv"
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['data'])
        print(df.head())
    
        df.to_csv(file_name, index=False)
    else:
        print(f"Error: {response.status_code}")

    df = pd.read_csv(file_name)
    print(df.describe())

    df.drop(['asd_code', 'watershed_desc', 'week_ending', 'state_fips_code', 'county_code', 'state_name', 'county_name', 'statisticcat_desc'], axis=1, inplace=True)
# %%
    df.head()

perStateData(state2abbrev)