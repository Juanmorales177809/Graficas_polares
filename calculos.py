
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import pandas as pd


#Data normalization
def normalize(df_input):
    maximo = max(df_input)
    return df_input - maximo

#Interpolation with splines
def interpolation(df_input,ang):
    evaluate = np.linspace(0,6.28,360)
    df_input = df_input.to_numpy()
    gain = np.interp(evaluate,ang,df_input)
    return gain, evaluate

def gain(df):
    r1 = np.linspace(0,len(df)-1,len(df))
    r1 = pd.DataFrame(r1, columns=["ang"])
    r1.columns = ["ang"]
    index = np.argmin(df)
    value = np.min(df)
    
    return r1,value ,index
    
    






