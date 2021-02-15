from Clases.Datos import Datos

contador=0
identificador=None
numeros=[]
operaciones=[]
datos=[]
valorBuscar=0
operacionO=None
operacionB=None
splt=None

def leerArchivo(ruta):
    datos.clear()
    print("\n----------------------------------CARGAR ARCHIVO----------------------------------\n")
    global contador
    archivo=open(ruta,'r')
    for linea in archivo.readlines():
        #print("\nSalida linea "+str(contador)+":")
        obtenerIdentificador(linea)
        contador+=1
    archivo.close()
    print(" > Archivo cargado con éxito")
    input("\n- PRESIONE ENTER PARA CONTINUAR...")

def obtenerIdentificador(linea):
    global identificador
    splt=linea.split("=")
    identificador=splt[0].replace(" ","")
    #print(" > Identificador = "+identificador)
    obtenerNumeros(splt[1])

def obtenerNumeros(txt):
    #if txt.startswith(" "):
        #txt=txt.replace(" ","",1)
    global numeros
    s=txt.replace(" ","")
    if 'B' in s:
        s=s.replace("B"," B")
    if 'O' in s:
        s=s.replace("O"," O")
    n=s.split(" ",1)
    numeros=n[0].split(",")
    for x in range(len(numeros)):
        numeros[x] = int(numeros[x])
    #print(" > Lista_numeros = ",numeros)
    obtenerOperaciones(n[1])

def obtenerOperaciones(op):
    #q=op.split(",")
    global operacionB
    global operacionO
    if 'BUSCAR' in op:
        operacionB="BUSCAR"
    else:
        operacionB=None

    if 'ORDENAR' in op:
        operacionO="ORDENAR"
    else:
        operacionO=None
    '''
    if operacionO!=None:
        operaciones.append(operacionO)
        
    if operacionB!=None:
        operaciones.append(operacionB)

    print(" > Lista_palabras_reservadas = ",operaciones)
    operaciones.clear()'''
    obtenerNumeroBuscar(op)
    #print(q[0].strip())

def obtenerNumeroBuscar(op):
    global valorBuscar
    op=op.replace("ORDENAR","")
    op=op.replace("BUSCAR","")
    op=op.replace(",","")
    op=op.replace(" ","")
    op=op.strip()
    #print(" > Valor_a_buscar = ",op)
    if op.isnumeric():
        valorBuscar=op
        valorBuscar=int(valorBuscar)
        #print(" > Valor_a_buscar = ",op)
    else:
        valorBuscar=None
    llenarDatos()

def llenarDatos():
    datos.append(Datos(contador, identificador, numeros, operacionO, operacionB,valorBuscar))

def getDatos():
    return datos