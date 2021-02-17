#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
#----------------------------------------------------CLASES--------------------------------------------------
from Funciones import Analizador
from Funciones import Funciones
from Funciones import Reportes

#----------------------------------------------VARIABLES GLOBALES--------------------------------------------
datos=[]
ruta=""
#-----------------------------------------------FILE CHOOSER-------------------------------------------------
def obtenerArchivo():
    global datos
    global ruta
    #Tk().withdraw() 
    try:
        ruta = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
        Analizador.leerArchivo(ruta)
        datos=Analizador.getDatos()
    except:
        print(" > ERROR: No se seleccionó ningún archivo o el archivo no cumple con el formato")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

#-------------------------------------------------MENU-------------------------------------------------------
def cargarArchivo():
    obtenerArchivo()

def listasOrdenadas():
    if ruta!="":
        Funciones.listasOrdenadas(datos)
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def busquedas():
    if ruta!="":
        Funciones.busquedas(datos)
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def todo():
    if ruta!="":
        Funciones.deplegarTodas(datos)
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def desplegarTodo():
    if ruta!="":
        Reportes.reporte(datos)
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def salir():
    print("  > Saliendo...\n")

def menu():
    opcion=0
    while opcion!=6:
        print("\n----------------------------------MENÚ PRINCIPAL----------------------------------\n")
        print(" 1. Cargar archivo de entrada")
        print(" 2. Desplegar listas ordenadas")
        print(" 3. Desplegar búsquedas")
        print(" 4. Desplegar todas")
        print(" 5. Desplegar todas a archivo")
        print(" 6. Salir\n")
        opcion=int(input("- Ingrese una opción:\n  > "))
        switch={1:cargarArchivo, 2: listasOrdenadas, 3: busquedas, 4: todo, 5: desplegarTodo, 6: salir}
        func=switch.get(opcion,"Opción inválida")
        try:
            func()
        except:
            print("\n > Opción inválida...")
            input(" - PRESIONE ENTER PARA CONTINUAR...")
menu()

