# -*- coding: utf-8 -*-

def leerArchivo(nombre):

    #.decode("utf-8"))
    archivo = open("plantillas/"+nombre + ".html")
    html=archivo.read().decode("UTF-8")
    return html
    
def llenarPlantilla(nombreArchivo,dicLlenador):
    
    html=leerArchivo(nombreArchivo)
    for key in dicLlenador.keys():
        html=html.replace("<!--"+key+"-->",dicLlenador[key])
    return html
 