import time
import json
import csv
import pandas as pd


localTime = time.asctime(time.localtime(time.time()))
print(localTime)
power = [0.13611587, 0.90992584, 0.416241  , 0.7313621 , 0.56836918,
       0.33141132, 0.6716091 , 0.80624722, 0.94958489, 0.44223749,
       0.25257855, 0.86695147, 0.7231505 , 0.4344175 , 0.2064644 ,
       0.27361311, 0.5655673 , 0.19780228, 0.08595054, 0.17408471]



def genDate():
    date = []
    for i in range(0,len(power)):
        date.append(time.asctime(time.localtime(time.time())))
    return date


def jsonCreate(date, power, text=""):
    try:
        dic = {"date" : date, "power": power}
        filename = text
        with open(filename,'w' ) as json_file:
            json.dump(dic,json_file)
            print("Archivo " + filename + " guardado")
    except :
        print("No se pudo guardar el archivo")
        
        
def csvCreates(date, power, text = ""):
    try:
        dic = {"date" : date, "power": power}
        df = pd.DataFrame(dic)
        filename = text
        df.to_csv(filename, mode = 'a',index=False, header=False,sep=';',decimal=',')
        print("Archivo "+filename+" creado con exito")
    except:
        print("No se pudo guardar el archivo")
            
'''--- Otra opción al csv -----'''
def csvCreate(date,power, text=""):
    try:
        fields = ['Date', 'Power']
        rows = []
        filename = text
        for i in range(0, len(power)):
            temp = [date[i],power[i]]
            rows.append(temp)
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file,dialect='unix')
            csv_writer.writerow(fields)
            csv_writer.writerows(rows)
            print("Archivo"+filename+"creado con exito")
    except :
        print("No se pudo guardar el archivo")


        
    
   
     
#jsonCreate(genDate(),power,"datos.json")
csvCreates(genDate(),power, "datos.csv")





