def listasOrdenadas(datos):
    print("\n----------------------------------LISTAS ORDENADAS----------------------------------")
    for ordenar in datos:
        if ordenar.getOperacionO()=="ORDENAR":
            aux=ordenar.getLista()
            s=aux.copy()
            s.sort()
            print("\n- ",ordenar.getIdentifiador(),":\n\n    > ORDENADOS = ",end="")
            print( ", ".join( repr(n) for n in s ) )
    input("\n- PRESIONE ENTER PARA CONTINUAR...")

def busquedas(datos):
    print("\n--------------------------------------BUSQUEDAS--------------------------------------")
    cont=0
    for buscar in datos:
        posiciones=[]
        if buscar.getOperacionB()=="BUSCAR":
            aux=buscar.getLista()
            numero=buscar.getNbuscar()
            print("\n- ",buscar.getIdentifiador(),":\n\n    > BUSQUEDA = ",end="")
            print( ", ".join( repr(n) for n in aux ) )
            print("    > VALOR A BUSCAR = ",buscar.getNbuscar())
            for posicion in aux:
                if posicion==numero:
                    posiciones.append(cont)
                cont+=1
            if len(posiciones)==0:
                print("    > POSICIONES = NO ENCONTRADO")
            else:
                print("    > POSICIONES = ",end="")
                print( ", ".join( repr(q) for q in posiciones ) )
            cont=0
    input("\n- PRESIONE ENTER PARA CONTINUAR...")

def deplegarTodas(datos):
    print("\n------------------------------------LISTAS PROCESADAS------------------------------------")
    for ordenar in datos:
        if ordenar.getOperacionO()=="ORDENAR":
            aux=ordenar.getLista()
            s=aux.copy()
            s.sort()
            print("\n- ",ordenar.getIdentifiador(),":\n\n    > ORDENADOS = ",end="")
            print( ", ".join( repr(n) for n in s ) )
            cont=0
           
            posiciones=[]
            if ordenar.getOperacionB()=="BUSCAR":
                aux=ordenar.getLista()
                numero=ordenar.getNbuscar()
                print("\n    > BUSQUEDA = ",end="")
                print( ", ".join( repr(n) for n in aux ) )
                print("    > VALOR A BUSCAR = ",ordenar.getNbuscar())
                for posicion in aux:
                    if posicion==numero:
                        posiciones.append(cont)
                    cont+=1
                if len(posiciones)==0:
                    print("    > POSICIONES = NO ENCONTRADO")
                else:
                    print("    > POSICIONES = ",end="")
                    print( ", ".join( repr(q) for q in posiciones ) )
                cont=0
    input("\n- PRESIONE ENTER PARA CONTINUAR...")