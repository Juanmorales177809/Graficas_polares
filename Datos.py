import csv
import pandas as pd
from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox


class Data:
    indice = -1
    datos = []
    campos = ["ratio", "abs[dBi]"]
    @staticmethod
    def obtener(nombreArchivo):
        with open(nombreArchivo,newline='') as archivoCSV:
            registros = csv.DictReader(archivoCSV,Data.campos, delimiter = ";")
            for i in registros:
                Data.datos.append(i)
            
     #Convertir los registros en una matriz de textos
    @staticmethod
    def pasarMatriz(r1 ,data):
        datos = []
        for cn in range(0,len(r1)):
            datos.append([data[cn],r1[cn]])
        return datos          

    #Método para Agregar un Dato
    @staticmethod
    def agregar(angulo, ganancia):
        c = dict(zip(Data.campos, [angulo, ganancia]))
        Data.datos.append(c)

    #Método para Modificar un Contacto
    @staticmethod
    def modificar():
        global datos
        
        if Data.indice in range(0, len(Data.datos)):
            Data.datos[Data.indice]=dict(zip(Data.campos, [angulo, ganancia]))

    #Método para Eliminar un Contacto
    @staticmethod
    def eliminar():
        if Data.indice in range(0, len(Data.datos)):
            del Data.datos[Data.indice]

    #Método para Guardar los Contactos en un archivo
    @staticmethod
    def guardar(nombreArchivo):
        with open(nombreArchivo, "w", newline='') as archivoCSV:
            registros = csv.DictWriter(archivoCSV, fieldnames=Contacto.campos, delimiter=";")
            for c in Data.datos:
                registros.writerow(c)
    @staticmethod
    def leerDatos(text):
        df = pd.read_csv(text, sep = ';', decimal=",")
        df.columns=["Ang", "dBm"]
        ang = np.linspace(0,6.28,73)
        dBm = df["dBm"]
        return r1, gain
    @staticmethod
    def leerDatosSimula(text):
        try:
            df = pd.read_fwf(text, sep = ";", decimal = "." )
            df = df.dropna(1, how = "all")
            df.columns = ["Theta1","Phi","Gain","Theta","Phase_Theta","Phi","Phase_Phi","AxRatio"]
            gain = df["Gain"]
            r1 = np.linspace(0,6.28,360)
            return r1, gain
        except:
            print("")
            
    @staticmethod
    def crearCsv(data,r1):
        
        try:
            dic = {"angulo" : r1, "ganancia": data}
            df = pd.DataFrame(dic)
            filename = "polaroid.csv"
            df.to_csv(filename, mode = 'a',index=False, header=False,sep=';',decimal='.')
            print("Archivo "+filename+" creado con exito")
        except:
            print("No se pudo guardar el archivo")
        Data.obtener("polaroid.csv")
    @staticmethod
    def graficar(r1,gain):
        plt.rc('grid', color='black', linewidth=0.5, linestyle='--')
        plt.rc('xtick', color='black',labelsize=10)
        plt.rc('ytick', color='red',labelsize=10)
        ax = plt.subplot(111, projection='polar')
        ax.plot(r1,gain,color='blue', ls='-', lw=1, label='2.4GHz')
        ax.legend()
        plt.suptitle("Patron de radiación",fontsize=20)
        plt.show()
    
       
        
    @staticmethod
    def abrirArchivo():
        root = Tk() 
        root.withdraw() 
        file_path = filedialog.askopenfilename(title = "Abrir Archivo",filetypes = (("Archivos de texto","*.txt"),\
                                                                                   ("Archivos de datos","*.csv"),\
                                                                                    ("Todos los qrchivos","*.*")))
        return file_path 
           
        
        
