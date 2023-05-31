# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:29:38 2021

@author: JUANCARLOSMORALESGUERRA
"""
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
import Util
from Datos import Data
from tkinter import filedialog
from tkinter import messagebox

iconos = ["./iconos/agregar.png", \
          "./iconos/abrir.png",\
          "./iconos/editar.png", \
          "./iconos/guardar.png", \
          "./iconos/interpolar.png",\
          "./iconos/polar.png"]

textosTooltip = ["agregar datos",\
                 "abrir archivo",\
                 "modificar datos",\
                 "guardar los cambios realizados",\
                 "interpolar",\
                 "grafica polar"]

indiceBA = 3
indiceBC = 2
indiceBD = 4
indiceBE = 5
data = 0
r1 = 0
encabezados = ["ratio","abs[dBi]"]
paneles = []
tDatos = None
muestra = False


#subrutina que cambia el ambiente de LISTAR a EDITAR y viceversa
def habilitar(editando):
    global indiceBA, indiceBC, indiceBD
    #Cambiar el estado de los botones
    for i in range(0, len(botones)):
        if editando:
            if i!=indiceBA and i!=indiceBC:
                botones[i].configure(state=DISABLED)
            else:
                botones[i].configure(state=NORMAL)
        else:
            if i!=indiceBA and i!=indiceBC:
                botones[i].configure(state=NORMAL)
            else:
                botones[i].configure(state=DISABLED)
    #Desplegar el panel respectivo
    if len(nb.tabs())>0:
        nb.forget(0) #limpiar las pestañas
    if editando:
        nb.add(paneles[1], text="Editando Datos")
    else:
        nb.add(paneles[0], text="Listar Datos")
    nb.focus() #refrescar las pestañas
def habilitarPolar(abrir):
    global indiceBD
    global indiceBE
    for i in range(0, len(botones)):
        if abrir == False:
            botones[indiceBD].configure(state=DISABLED)
            botones[indiceBE].configure(state=DISABLED)
        else:
            botones[indiceBD].configure(state=NORMAL)
            botones[indiceBE].configure(state=NORMAL)
#Metodo que muestra los datos en una tabla
def mostrar(r1, data):
    try:
        global tDatos
        global muestra
        datos = Data.pasarMatriz(r1, data)
        muestra = True
        tContactos = Util.mostrarTabla(paneles[0], encabezados, datos, tDatos)
    except:
        print("No hay datos para mostrar")
v = Tk()
v.title("Graficas polares v.1.0")
v.geometry("450x325")
botones = Util.agregarBarra(v, iconos,textosTooltip)
nb = Notebook(v)
nb.pack(fill=BOTH, expand=YES)

paneles.append(Frame(v)) #panel de listado
paneles.append(Frame(v)) #panel de edición

habilitar(False)
habilitarPolar(False)

def abrir():
    return filedialog.askopenfilename(title = "Abrir Archivo",filetypes = (("Archivos de texto","*.txt"),("Archivos de datos","*.csv"),("Todos los archivos","*.*")))
    
def archivo(abrir):
    try:
        global data
        global r1
        data,r1 = Data.leerDatosSimula(abrir)
        mostrar(r1,data)
        habilitarPolar(True)
    except:
        print("")
def nada():
    messagebox.showinfo(message="Este boton está en construcción", title="No se preocupe")
def ventana():
    v = Tk()
    v.title("Crear datos experimentales")
    v.geometry("350x200")
          
botones[1].configure( command=lambda:archivo(abrir()))    
botones[5].configure(command=lambda: Data.graficar(data,r1))
botones[0].configure(command=lambda:archivo(ventana()))
botones[2].configure(command=lambda:archivo(nada()))
botones[3].configure(command=lambda:archivo(nada()))
botones[4].configure(command=lambda:archivo(nada()))

v.mainloop()





















