contador=0
identificador=None
numeros=[]
operaciones=[]
valorBuscar=0
operacionO=None
operacionB=None
splt=None

def leerArchivo(ruta):
    global contador
    archivo=open(ruta,'r')
    for linea in archivo.readlines():
        print("\nSalida linea "+str(contador)+":")
        obtenerIdentificador(linea)
        contador+=1
    archivo.close()

def obtenerIdentificador(linea):
    splt=linea.split("=")
    identificador=splt[0]
    print(" > Identificador = "+identificador)
    obtenerNumeros(splt[1])

def obtenerNumeros(txt):
    if txt.startswith(" "):
        txt=txt.replace(" ","",1)
    n=txt.split(" ",1)
    numeros=n[0].split(",")
    print(" > Lista_numeros = ",numeros)
    obtenerOperaciones(n[1])

def obtenerOperaciones(op):
    #q=op.split(",")
    if 'BUSCAR' in op:
        operacionB="BUSCAR"
    else:
        operacionB=None

    if 'ORDENAR' in op:
        operacionO="ORDENAR"
    else:
        operacionO=None

    if operacionO!=None:
        operaciones.append(operacionO)
        
    if operacionB!=None:
        operaciones.append(operacionB)

    print(" > Lista_palabras_reservadas = ",operaciones)
    operaciones.clear()
    #print(q[0].strip())

    