# -*- coding: utf-8 -*-
"""
Radiation pattern graphing program
This module uses methods that read files exported in CST in .txt format and experimental in .csv
It is a plug-in module for the GUI program "polarGraphicsMain.py"
find more information is https://github.com/Juanmorales177809/crudMedir.git
Created on Wed Dec  8 08:46:48 2021
@author: JUANCARLOSMORALESGUERRA for the ITM fiber optic and antennas seedbed
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline



#Function that reads the experimental data and returns two vectors
def readData(text):
    df = pd.read_csv(text, sep = ';', decimal=",")
    df.columns=["Ang", "dBm"]
    ang = np.linspace(0,6.28,73)
    dBm = df["dBm"]
    dBm,ang = interpolation(dBm,ang)
    dBm = normalize(dBm)
    return ang, dBm
#Function that reads simulated data in CST and returns two vectors


def readSimulatedData(text):
    df = pd.read_fwf(text, sep = ";", decimal = "." )
    df = df.dropna(how='all')
    df.columns = ["Theta1","Phi","Gain","Theta","Phase_Theta","Phi","Phase_Phi","AxRatio"]
    df = df["Gain"]
    df = normalize(df)#data normalization
    r1 = np.linspace(0,6.28,360)
    return r1, df

def leerDatosSimulacion(text):
    df = pd.read_fwf(text, sep = " ", decimal = "." )
    df = df.dropna(how='all')
    
    for i in df.columns:
        if i == "Abs(Theta)[dBi   ]":
            col = i
    df = df[col]
    
    df = normalize(df)
    r1 = np.linspace(0,6.28,360)
    return r1, df

#Normalization by quartiles
def quantile_norm(df_input):
    sorted_df = pd.DataFrame(np.sort(df_input.values,axis=0), index=df_input.index, columns=df_input.columns)
    mean_df = sorted_df.mean(axis=1)
    mean_df.index = np.arange(1, len(mean_df) + 1)
    quantile_df =df_input.rank(method="min").stack().astype(int).map(mean_df).unstack()
    df_input.ra
    return(quantile_df)
#Data normalization
def normalize(df_input):
    maximo = max(df_input)
    return df_input - maximo
#Interpolation with splines
def interpolation(df_input,ang):
    evaluate = np.linspace(0,6.28,len(df_input))
    gain = InterpolatedUnivariateSpline(ang, df_input)(evaluate)
    return gain, evaluate
    
#Comparative polar graphs
def comparativePolarGraph(a1,b1,r1,theta,a2,b2,r2,theta2,a3,b3,r3,theta3,a4,b4,r4,theta4,text,text1,text2,vec,vecs):
    
    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.set_size_inches(8,8)
    plt.rc('grid', color='black', linewidth=0.5, linestyle='--')
    plt.rc('xtick', color='black',labelsize=10)
    plt.rc('ytick', color='black',labelsize=10)
    ax[0, 0]= plt.subplot(221, projection='polar')
    ax[0, 1] = plt.subplot(222, projection='polar')
    ax[1, 0] = plt.subplot(223, projection='polar')
    ax[1, 1]= plt.subplot(224, projection='polar')
    ax[0, 0].set_rticks(vecs)
    ax[0, 0].plot(a1,b1, ls=':',color="blue" ,lw=2, label=text1)
    ax[0, 0].plot(r1,theta,color='red', ls='-', lw=2, label= text2)
    ax[0, 0].set_title("(a)", y=-0.1, x= 0)
    ax[0, 1].plot(a2,b2,color='blue', ls=':', lw=2,label=text1)
    ax[0, 1].plot(r2,theta2,color='red', ls='-', lw=2,label=text2)
    ax[0, 1].set_rticks(vec)
    ax[0, 1].set_title("(b)", y=-0.1, x= 0)
    ax[1, 0].plot(a3,b3,color='blue', ls=':', lw=2,label=text1)
    ax[1, 0].plot(r3,theta3,color='red', ls='-', lw=2,label=text2)
    ax[1, 0].set_rticks(vec)
    ax[1, 0].set_title("(c)", y=-0.1, x= 0)
    ax[1, 1].plot(a4,b4,color='blue', ls=':', lw=2, label=text1)
    ax[1, 1].plot(r4,theta4,color='red', ls='-', lw=2, label=text2)
    ax[1, 1].set_rticks(vec)
    ax[1, 1].set_title("(d)", y=-0.1, x= 0)
    plt.suptitle(text,fontsize=20)
    ax[1, 1].legend(loc=4)
    plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)
    plt.show()

#Simple polar graphs
def simplePlarGraph(a1,b1,a2,b2,a3,b3,a4,b4,text,color):
    fig, ax = plt.subplots(2,2)
    fig.set_size_inches(8,8)
    plt.rc('grid', color='black', linewidth=0.5, linestyle='--')
    plt.rc('xtick', color='black',labelsize=10)
    plt.rc('ytick', color='red',labelsize=10)
    ax = plt.subplot(221, projection='polar')
    ax1 = plt.subplot(222, projection='polar')
    ax2 = plt.subplot(223, projection='polar')
    ax3 = plt.subplot(224, projection='polar') 
    ax.plot(a1,b1,color=color, ls='-', lw=1, label='2.4Ghz')
    ax.legend()
    ax1.plot(a2,b2,color=color, ls='-', lw=1, label='2.4Ghz')
    ax1.legend()
    ax2.plot(a3,b3,color=color, ls='-', lw=1, label='2.4Ghz')
    ax2.legend()
    ax3.plot(a4,b4,color=color, ls='-', lw=1, label='2.4Ghz')
    ax3.legend()
    plt.suptitle(text,fontsize=20)
    plt.show()


#main   
a1,b1 = readData("./Data/port1.csv")
a2,b2 = readData("./Data/port2.csv") 
a3,b3 = readData("./Data/port3.csv")
a4,b4 = readData("./Data/port4.csv") 

r1,theta = readData("./Data/port1meta.csv")
r2,theta2 = readData("./Data/port2meta.csv")
r3,theta3 = readData("./Data/port3meta.csv")
r4,theta4 = readData("./Data/port4meta.csv")

A1,B1 = leerDatosSimulacion("./Data/port1S.txt")
A2,B2 = leerDatosSimulacion("./Data/port2S.txt") 
A3,B3 = leerDatosSimulacion("./Data/port3S.txt")
A4,B4 = leerDatosSimulacion("./Data/port4S.txt") 

R1,Theta = leerDatosSimulacion("./Data/port1metaS.txt")
R2,Theta2 = leerDatosSimulacion("./Data/port2metaS.txt")
R3,Theta3 = leerDatosSimulacion("./Data/port3metaS.txt")
R4,Theta4 = leerDatosSimulacion("./Data/port4metaS.txt")

# A1,B1 = readSimulatedData("./Data/port1S.txt")
# A2,B2 = readSimulatedData("./Data/port2S.txt") 
# A3,B3 = readSimulatedData("./Data/port3S.txt")
# A4,B4 = readSimulatedData("./Data/port4S.txt") 

# R1,Theta = readSimulatedData("./Data/port1metaS.txt")
# R2,Theta2 = readSimulatedData("./Data/port2metaS.txt")
# R3,Theta3 = readSimulatedData("./Data/port3metaS.txt")
# R4,Theta4 = readSimulatedData("./Data/port4metaS.txt")

vec = [-30,-20,-10,0,10]
vec2 = [-50,-40,-30,-20, -10,0,10]
vec3 = [-50,-40,-30,-20,-10]
# comparativePolarGraph(a1,b1,r1,theta,a2,b2,r2,theta2,a3,b3,r3,theta3,a4,b4,r4,theta4,"","Without MTM","With MTM",vec3,vec3)
comparativePolarGraph(a1,b1,A1,B1,a2,b2,A2,B2,a3,b3,A3,B3,a4,b4,A4,B4,"","Experiment without MTM","Simulated without MTM",vec,vec2)
comparativePolarGraph(r1,theta,R1,Theta,r2,theta2,R2,Theta2,r3,theta3,R3,Theta3,r4,theta4,R4,Theta4,"","Experiment with MTM","Simulated with MTM",vec,vec2)
#simplePlarGraph(a1,b1,a2,b2,a3,b3,a4,b4, 'Matriz de Butler Metamateriales experimental','blue')
#simplePlarGraph(r1,theta,r2,theta2,r3,theta3,r4,theta4,'Matriz de Butler metamateriales simulada','green')   
"""
a1,b1 = readData("./Data/port1.csv")
a2,b2 = readData("./Data/port2.csv") 
a3,b3 = readData("./Data/port3.csv")
a4,b4 = readData("./Data/port4.csv")
r1,theta = readSimulatedData("./Data/port1S.txt")
r2,theta2 = readSimulatedData("./Data/port2S.txt")
r3,theta3 = readSimulatedData("./Data/port3S.txt")
r4,theta4 = readSimulatedData("./Data/port4S.txt")
simplePlarGraph(a1,b1,a2,b2,a3,b3,a4,b4, 'Matriz de Butler convencional experimental','blue')
simplePlarGraph(r1,theta,r2,theta2,r3,theta3,r4,theta4,'Matriz de Butler convencional simulada','green')  
"""