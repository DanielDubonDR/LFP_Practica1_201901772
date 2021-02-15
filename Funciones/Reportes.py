import os
texto=""
def cabecera():
    global texto
    c="""<!DOCTYPE html>
        <html>
            <title>Reporte</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@400;700&family=Courgette&family=Lobster&family=Rokkitt:wght@300;800&display=swap" rel="stylesheet">
            <style>
                .w3-lobster 
                {
                    font-family: "Lobster", Sans-serif;
                }
                .Asap-Condensed
                {
                    font-family: 'Asap Condensed', sans-serif;
                }
                .Courgette
                {
                    font-family: 'Courgette', cursive;
                }
                .Rokkitt
                {
                    font-family: 'Rokkitt', serif;
                    font-weight: 800;
                }
            </style>
            <body>
                <div class="w3-container w3-teal w3-center w3-margin-bottom">
                    <br>
                    <h1 class="w3-lobster" style="font-size: 60px;">Reporte</h1>
                    <br>
                </div>
                <br>"""
    texto+=c

def crearArchivo():
    arhcivo=open('Reporte.html','w')
    arhcivo.write(texto)
    arhcivo.close()
    os.startfile("Reporte.html")

def reporte(datos):
    global texto
    cabecera()
    for ordenar in datos:
        texto+="""<div class="w3-container  w3-margin-bottom" >
            <div class="w3-card-4 w3-margin-bottom">
                <header class="w3-container w3-teal  w3-round-small">
                    <h1 class="Rokkitt">"""+str(ordenar.getIdentifiador())+""":</h1>
                </header>"""
        if ordenar.getOperacionO()=="ORDENAR":
            aux=ordenar.getLista()
            s=aux.copy()
            s.sort()
            texto+="""<div class="w3-container w3-middle Asap-Condensed">
                    <p class="w3-center" style="font-size: 20px; font-weight: 500;">Lista ordenada</p>
                    <hr>
                    <p>> ORDENADOS = """
            txt=""
            for n in s:
                txt+=str(n)+", "
            txt=txt.rstrip(", ")
            texto+=txt
            texto+=" </p>"
        else:
            texto+="""<div class="w3-container w3-middle Asap-Condensed">"""   

        cont=0
        posiciones=[]
        if ordenar.getOperacionB()=="BUSCAR":
            texto+="""<p class="w3-center" style="font-size: 20px; font-weight: 500;">Búsquedas</p>
                    <hr>
                    <p>> BUSQUEDA = """
            aux=ordenar.getLista()
            numero=ordenar.getNbuscar()
            q=""
            for n in aux:
                q+=str(n)+", "
            texto+=q.rstrip(", ")
            texto+="</p><p>> VALOR A BUSCAR = "
            texto+=str(ordenar.getNbuscar())+"</p>"
            for posicion in aux:
                if posicion==numero:
                    posiciones.append(cont)
                cont+=1
            if len(posiciones)==0:
                texto+="<p> > POSICIONES = NO ENCONTRADO</p>" 
            else:
                texto+="<p>  > POSICIONES = "
                w=""
                for o in posiciones:
                    w+=str(o)+", "
                texto+=w.rstrip(", ")+"</p>"
        
            cont=0
        texto+="""</div>
                <footer class="w3-container w3-teal  w3-round-small">
                    <br>
                </footer>
            </div>
            <br></div>"""
    texto+="""</div>
    </body>
</html>"""
    crearArchivo()
    #print(texto)