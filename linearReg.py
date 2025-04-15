import numpy as np

#https://www.geeksforgeeks.org/linear-regression-python-implementation/
def estimate_coef(x, y):
 # number of observations/points
 n = np.size(x)

# mean of x and y vector
 m_x = np.mean(x)
 m_y = np.mean(y)

# calculating cross-deviation and deviation about x
 SS_xy = np.sum(y*x) - n*m_y*m_x
 SS_xx = np.sum(x*x) - n*m_x*m_x

# calculating regression coefficients
 b_1 = SS_xy / SS_xx
 b_0 = m_y - b_1*m_x

 return (b_0, b_1)


def runLinearReg():
    
# Load the CSV file into a DataFrame
   df = pd.read_csv('1970 zindex data.csv')
   data = df.to_numpy()
   
   df2 = pd.read_csv('nass_corn_yield_IA.csv')
   y = df2.to_numpy()
    
   coef = estimate_coef(data,y)
   print(coef)