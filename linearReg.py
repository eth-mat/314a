import numpy as np
import pandas as pd

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

def test():
    with open(r"C:\Users\mbrag\OneDrive\Documents\314A\314a\314 data\1970 zindex data.csv", 'r') as file:
        for i in range(10):
            print(file.readline())

def runLinearReg():
 
    df = pd.read_csv(
        r"C:\Users\mbrag\OneDrive\Documents\314A\314a\314 data\1970 zindex data.csv",
        comment='#',
        sep=",",
        engine='python'
    )
    x = pd.to_numeric(df["Value"], errors='coerce').to_numpy()

    df2 = pd.read_csv('nass_corn_yield_IA.csv', low_memory=False)

    print("Unique values in 'Value' column of corn data:", df2["Value"].unique())

    # Try to clean and convert "Value" column to numeric
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


