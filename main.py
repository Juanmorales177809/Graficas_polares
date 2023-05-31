"""
Radiation pattern graphing program
This module uses methods that read files exported in CST in .txt format and experimental in .csv
It is a plug-in module for the GUI program "polarGraphicsMain.py"
find more information is https://github.com/Juanmorales177809/crudMedir.git

Created on Wed Dec  8 08:46:48 2021

@author: JUANCARLOSMORALESGUERRA for the ITM fiber optic and antennas seedbed
"""



import os
import interpolando as itp
import calculos as cal
import pandas as pd



os.system("cls")
vec = [-30,-20,-10,0,10]
vec2 = [-50,-40,-30,-20, -10,0,10]
vec3 = [-50,-40,-30,-20,-10]
#main   
a1,b1 = itp.readData("./Data/port1.csv")
a2,b2 = itp.readData("./Data/port2.csv") 
a3,b3 = itp.readData("./Data/port3.csv")
a4,b4 = itp.readData("./Data/port4.csv") 

r1,theta = itp.readData("./Data/port1meta.csv")
r2,theta2 = itp.readData("./Data/port2meta.csv")
r3,theta3 = itp.readData("./Data/port3meta.csv")
r4,theta4 = itp.readData("./Data/port4meta.csv")

a1 = itp.normalize(a1)
a2 = itp.normalize(a2)
a3 = itp.normalize(a3)
a4 = itp.normalize(a4)

r1 = itp.normalize(r1)
r2 = itp.normalize(r2)
r3 = itp.normalize(r3)
r4 = itp.normalize(r4)

itp.comparativePolarGraph(a1,b1,r1,theta,a2,b2,r2,theta2,a3,b3,r3,theta3,a4,b4,r4,theta4,"","Without MTM","With MTM",vec3,vec3)

A1,B1 = itp.readSimulatedData("./Data/port1S.txt")
A2,B2 = itp.readSimulatedData("./Data/port2S.txt") 
A3,B3 = itp.readSimulatedData("./Data/port3S.txt")
A4,B4 = itp.readSimulatedData("./Data/port4S.txt") 

R1,Theta = itp.readSimulatedData("./Data/port1metaS.txt")
R2,Theta2 = itp.readSimulatedData("./Data/port2metaS.txt")
R3,Theta3 = itp.readSimulatedData("./Data/port3metaS.txt")
R4,Theta4 = itp.readSimulatedData("./Data/port4metaS.txt")


# gain = round(itp.gain(b1)[0])
r1 = itp.gain(b1)[1]

# print(gain)

itp.comparativePolarGraph(a1,b1,A1,B1,a2,b2,A2,B2,a3,b3,A3,B3,a4,b4,A4,B4,"","Experiment without MTM","Simulated without MTM",vec,vec2)
itp.comparativePolarGraph(r1,theta,R1,Theta,r2,theta2,R2,Theta2,r3,theta3,R3,Theta3,r4,theta4,R4,Theta4,"","Experiment with MTM","Simulated with MTM",vec,vec2)



# dic_gain={"Parameter": ["Gain", "Direction"],"port1": [cal.gain(a1)),b1[index]],"port2":[cal.gain(a2),b2),
#             ang2],"port3":[float(round(gain3)),ang3],"port4":[float(round(gain4)),ang4]}

dic_gain= {"Parameter": ["Gain", "Angle"],"port1": [round(itp.gain(b1)[0]), itp.gain(b1)[1]],"port2":[round(itp.gain(b2)[0]), itp.gain(b2)[1]],
           "port3":[round(itp.gain(b3)[0]), itp.gain(b3)[1]],"port4": [round(itp.gain(b4)[0]), itp.gain(b1)[1]]}

# dic_gain1={"port1": [float(round(calc.gain(dBm5)[2]))],"port2":[float(round(calc.gain(dBm6)[2]))],
#            "port3":[float(round(calc.gain(dBm7)[2]))],"port4":[float(round(calc.gain(dBm8)[2]))]}
df = pd.DataFrame(dic_gain)
# df1 = pd.DataFrame(dic_gain1)
