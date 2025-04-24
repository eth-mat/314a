#%% Imports
import pandas as pd
import numpy as np 
import geopandas as gpd
import matplotlib.pyplot as plt

# %%
crop_yield = pd.read_csv('US Crop Yield (in $) by County, 1997-2022.csv')
crop_yield = crop_yield[['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']]




# %%
years = np.arange(1970, 2025)
dfs = {}
for year in years:
    dfs[year] = pd.read_csv(f'314 data/{year} zinde data.csv')

# %%
