contador=0
identificador=None
numeros=[]
operaciones=[]
valorBuscar=0
operacionO=None
operacionB=None
splt=None

def leerArchivo(ruta):
    print("\n---------------------------------ARCHIVO ANALIZADO---------------------------------\n")
    global contador
    archivo=open(ruta,'r')
    for linea in archivo.readlines():
        print("\nSalida linea "+str(contador)+":")
        obtenerIdentificador(linea)
        contador+=1
    archivo.close()
    input("\n- PRESIONE ENTER PARA CONTINUAR...")

def obtenerIdentificador(linea):
    splt=linea.split("=")
    identificador=splt[0]
    print(" > Identificador = "+identificador)
    obtenerNumeros(splt[1])

def obtenerNumeros(txt):
    #if txt.startswith(" "):
        #txt=txt.replace(" ","",1)
    s=txt.replace(" ","")
    if 'B' in s:
        s=s.replace("B"," B")
    if 'O' in s:
        s=s.replace("O"," O")
    n=s.split(" ",1)
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
    obtenerNumeroBuscar(op)
    #print(q[0].strip())

def obtenerNumeroBuscar(op):
    op=op.replace("ORDENAR","")
    op=op.replace("BUSCAR","")
    op=op.replace(",","")
    op=op.replace(" ","")
    op=op.strip()
    #print(" > Valor_a_buscar = ",op)
    if op.isnumeric():
        print(" > Valor_a_buscar = ",op)