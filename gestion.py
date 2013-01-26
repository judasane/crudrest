# -*- coding: utf-8 -*-
from cherrypy._cpchecker import Checker
import database
import templater
import generadorHtml as genHtml

def registrar(modulo):
    dic = {}
    retorno = ""
    tabla = ""
    if modulo == "usuarios":
        tabla = "roles"
    elif modulo == "roles":
        tabla = "permissions"
    if tabla != "":
        select = genHtml.llenarSelectBD(tabla)
        dic = {"opciones":select}
        retorno = templater.llenarPlantilla(modulo + "/registro", dic)
    else:
        retorno = templater.leerArchivo(modulo + "/registro")
    return retorno

def listar(modulo):
    dic={}
    lista=[]
    retorno=""
    dicTablas={"usuarios":"users","roles":"roles","permisos":"permissions"}
    if modulo=="usuarios".lower():
        lista=["ID","Nombre","Apellido","Username","Email"]
    elif modulo=="roles".lower():
        lista=["ID","Nombre","Descripcion"]
    elif modulo=="permisos".lower():
        lista=["ID","Nombre","Descripcion"]
    dic["tabla"]=genHtml.llenarTablaBD(dicTablas[modulo],lista,True)
    
    retorno=templater.llenarPlantilla("general/listar", dic)
    return retorno

def eliminar(modulo,id):
    db=database.DatabaseManager("WeBD","MySql")
    return db.eliminar(modulo,id)

if __name__ == "__main__":
    print llenarTabla("users")
