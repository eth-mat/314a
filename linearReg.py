import numpy as np
import pandas as pd
import os 


#TODO: figure out how to pair the grab the correct year and area in yield to compare to correct val and area in z-index
#TODO: put above info into a cvs for geoplotzindex to read from and follow directions from plotly. 


# Estimate coefficients for linear regression
def estimate_coef(x, y):
    # number of observations
    n = np.size(x)

    # means of x and y
    m_x = np.mean(x)
    m_y = np.mean(y)

    # cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)



def runLinearReg():
    
    # Assign directory
    dataDirectory = r"C:\Users\mbrag\OneDrive\Documents\314A\314a\314 data"

# Iterate over files in directory
    for name in os.listdir(dataDirectory):
    # Open file
        with open(os.path.join(dataDirectory, name)) as f:
            df = pd.read_csv(f,
            comment='#',
            sep=",",
            engine='python'
    )
        x = pd.to_numeric(df["Mean"], errors='coerce').to_numpy()
        cropDirectory = r"C:\Users\mbrag\OneDrive\Documents\314a\Crop Yield by State (csv)" 
        for name in os.listdir(cropDirectory):
    # Open file
            with open(os.path.join(cropDirectory, name)) as f2:
                df = pd.read_csv(f,
                comment='#',
                sep=",",
                engine='python'
    )
            df2 = pd.read_csv(f2, low_memory=False)
            y = pd.to_numeric(df2["Value"].astype(str).str.replace(',', ''), errors='coerce').to_numpy()

    min_len = min(len(x), len(y))
    x = x[:min_len]
    y = y[:min_len]

    mask = ~np.isnan(x) & ~np.isnan(y)
    x = x[mask]
    y = y[mask]

    print("x sample:", x[:5])
    print("y sample:", y[:5])

    b_0, b_1 = estimate_coef(x, y)
    print(f"Estimated coefficients:\nb_0 = {b_0:.4f} \nb_1 = {b_1:.4f}")



# Run the regression
runLinearReg()

