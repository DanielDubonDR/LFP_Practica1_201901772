contador=0
identificador=None
numeros=[]
operacionO=None
operacionB=None
splt=None

def leerArchivo(ruta):
    global contador
    archivo=open(ruta,'r')
    for linea in archivo.readlines():
        obtenerIdentificador(linea)
        contador+=1
    archivo.close()

def obtenerIdentificador(linea):
    splt=linea.split("=")
    identificador=splt[0]
    obtenerNumeros(splt[1])

def obtenerNumeros(txt):
    if txt.startswith(" "):
        txt=txt.replace(" ","",1)
    n=txt.split(" ",1)
    numeros=n[0].split(",")
    obtenerOperaciones(n[1])

def obtenerOperaciones(op):
    q=op.split(",")
    print(q[0].strip())
    