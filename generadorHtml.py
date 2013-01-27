# -*- coding: utf-8 -*-
import database
import os
def llenarSelectBD(tabla):
    """Llena un select con los nombres de una tabla.

    Recibe como parÃ¡metro un string con el nombre de la tabla que contiene los
    nombres deseados.

    Retorna un string con el cÃ³digo html listo para emplazar en el contenido de
    un select
    """

    bd = database.DatabaseManager()
    dicc={}
    lista=bd.obtenerDatos(tabla)
    for registro in lista:
        dicc[registro["nombre"]]=registro["id"]
    options=llenarSelect(dicc)

    return options


def llenarSelect(diccionario):
    """Llena un select con los valores de un diccionario.

    Recibe como parámetro un diccionario con el formato {"nombre":"valor"}, con
    los que se llenarÃ¡ el select.

    Retorna un string con el código html listo para emplazar en el contenido de
    un select
    """

    selectHtml = ""
    for item in diccionario:
        selectHtml += '<option value="%s">%s</option>\n' % (str(diccionario[item]), item)
    return selectHtml






def llenarTablaBD(tabla,listaCampos,ud=0):
    """Llena una tabla html a partir de los registros en la base de datos.

    Recibe como parÃ¡metro "tabla", que es el nombre de la tabla como string y
    "listaCampos", una lista con el nombre de los campos a llenar

    Retorna un string con una tabla html que contiene los registros de la tabla
    indicada
    """
    bdm = database.DatabaseManager()
    listaDiccionarios=bdm.obtenerDatos(tabla)

    listaResultado=[listaCampos]
    for diccionario in listaDiccionarios:
        #se crean sublistas
        subLista=[]
        for valor in listaCampos:
            subLista.append(diccionario[valor.lower()])
        if ud:
            id=diccionario["id"]
            botones="""<a href='editar/%s'><img alt='Editar' title='Editar'
            src='https://dl.dropbox.com/u/36392791/edit.png'></a>
            <a href='eliminar/%s'><img alt='Eliminar' title='Eliminar'
            src='https://dl.dropbox.com/u/36392791/delete.png'></a>""" % (id,id)
            subLista.append(botones)
#             subLista.append("<a href='eliminar/%s'><img alt='Eliminar' title='Eliminar' src='https://dl.dropbox.com/u/36392791/delete.png'></a>" % diccionario["id"] )
#            subLista.append("hola")
        listaResultado.append(subLista)
    if ud:
        listaResultado[0].append("Accionn")
        #listaResultado[0].append("Eliminar")

    return llenarTabla(listaResultado)




def llenarTabla(listaTabla):
    """
    A partir de una lista devuelve el cÃ³digo html necesario para una tabla.

    Recibe como parÃ¡metro una lista de listas cuyo primer Ã­tem es una lista con
    los nombres de las columnas de la tabla y los demÃ¡s itemas son listas con los
    valores respectivos de cada renglÃ³n.

    Retorna un string con el cÃ³digo html listo de una tabla llena.
    """
#Llena el renglÃ³n de headers de la tabla
    html="<table border=1>\n"
    iterador=0
    for renglon in listaTabla:
        html+="    <tr>\n"
        if iterador==0:
            for nombre in renglon:
                html+="        <th>%s</th>\n" % nombre
        else:
            for valor in renglon:
                html+="        <td>%s</td>\n" % valor
        html+="    </tr>\n"
    html+="</table>"
    return html

if __name__ == "__main__":
    print os.environ["PORT"] 
    print os.environ["IP"] 
    