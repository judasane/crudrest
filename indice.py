# -*- coding: utf-8 -*-
import database
import templater
import gestion as mod

class SitioWeb:
    "Clase que contiene los metodos principales para mostrar en el sitio web"


    def index (self , nombre="bienvenido"):
        'Pagina de inicio del sitio web, muestra la ruta que le sea asignada.'
        print "imprime"
        return templater.leerArchivo(nombre)

    def gestion(self,modulo,accion="index",parametro=None):
        "Metodo de gestion general"
        retorno=""
        if accion=="registrar":
            retorno=mod.registrar(modulo)
        elif accion=="listar":
            retorno=mod.listar(modulo)
        elif accion=="eliminar":
            retorno=mod.eliminar(modulo, parametro)
        else:
            retorno = templater.leerArchivo(modulo+"/"+accion)
        return retorno

    def recibirRegistro(self,formulario,nombre,apellido="",username="",email="",password="",role="",descripcion="",permisos=""):
        "Recibe los datos de registro por post"
        bd=database.DatabaseManager("webd","MySql")
        html=""
        if formulario=="usuarios":
            bd.crearUsuario(nombre,apellido,username,email,password,role)
            dic={"nombre":nombre,"apellido":apellido,"username":username,"email":email,"password":password}
            html=templater.llenarPlantilla("datos_recibidos_user",dic)
        elif formulario=="roles":
            bd=database.DatabaseManager("webd","Mysql")
            bd.crearRol(nombre,descripcion,permisos)
            dic={"nombre":nombre,"descripcion":descripcion}
            html=templater.llenarPlantilla("datos_recibidos_role",dic)
            
        elif formulario=="permisos":
            bd.crearPermiso(nombre,descripcion)
            dic={"nombre":nombre,"descripcion":descripcion}
            html=templater.llenarPlantilla("datos_recibidos_permission",dic)
        return html

    def pruebas(self,permisos):
        if type(permisos)==dict:
            retorno="Es un diccionario"
        elif type(permisos)==list:
            retorno="Es na lista"
        return retorno

    pruebas.exposed=True
    gestion.exposed=True
    recibirRegistro.exposed=True
    index.exposed = True

if __name__ == "__main__":
    sit=SitioWeb()
    print sit.pruebas([])



