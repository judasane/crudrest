# -*- coding: utf-8 -*-

def leerArchivo(nombre):

    #.decode("utf-8"))
    archivo = open("plantillas/"+nombre + ".html")
    html=archivo.read().decode("UTF-8")
    return html
    
def llenarPlantilla(nombreArchivo,dicLlenador):
    """
    Recibe como parámetro un diccionario de la forma clave-valor, en el que la
    clave hace referencia a un marcador (comentario) a cambiar en un archivo
    html plano
    """
    html=leerArchivo(nombreArchivo)
    for key in dicLlenador.keys():
        html=html.replace("<!--"+key+"-->",dicLlenador[key])
    return html
 