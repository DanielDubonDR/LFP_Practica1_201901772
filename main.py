#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
#----------------------------------------------------CLASES--------------------------------------------------
from Funciones import Analizador

#-----------------------------------------------FILE CHOOSER-------------------------------------------------
def obtenerArchivo():
    #Tk().withdraw() 
    try:
        ruta = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
        Analizador.leerArchivo(ruta)
    except:
        print("\n> ERROR: No se selecciono ningun archivo")
        input("- PRESIONE ENTER PARA CONTINUAR...")
#-------------------------------------------------MENU-------------------------------------------------------
def cargarArchivo():
    obtenerArchivo()

def listasOrdenadas():
    print("Cargar Archivo")

def busquedas():
    print("Cargar Archivo")

def todo():
    print("Cargar Archivo")

def desplegarTodo():
    print("Cargar Archivo")

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
        opcion=int(input("- Ingrese una opción\n  > "))
        switch={1:cargarArchivo, 2: listasOrdenadas, 3: busquedas, 4: todo, 5: desplegarTodo, 6: salir}
        func=switch.get(opcion,"Opcion invalida")
        func()
menu()