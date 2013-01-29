# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from dtos import Usuario,Role,Permission,RolesPermissions, UsersRoles

class DatabaseManager:
    """
    Clase que se encarga de gestionar las comunicaciones con la base de datos.
    
    """
    Session = None
    ses = None
    
    def __init__(self, clave="Pruebas2013!"):
        
        engine = create_engine("mysql://sibismark:" + clave + "@sibismark.db.10388322.hostedresource.com/sibismark" + "?charset=utf8", echo=False)
        self.Session = sessionmaker(bind=engine)
        self.ses = self.Session()
        
    
    
    def obtenerDatos(self, tabla):
        """
        Devuelve los datos de una tabla por medio de una lista.

        Recibe como parámetro el nombre de la tabla a la cual acceder.

        Retorna una lista de diccionarios cada uno lleno con conjuntos clave-valor
        que hacen referencia a los atributos de los objetos dto propios de la
        consulta
        """
        lista = []
        consulta = None
        if tabla.lower() == "users":
            consulta = self.ses.query(Usuario)
        elif tabla.lower() == "permissions":
            consulta = self.ses.query(Permission)
        elif tabla.lower() == "roles":
            consulta = self.ses.query(Role)
        for instancia in consulta:
            diccionario = instancia.toDict()
            lista.append(diccionario)
        return lista

    def crearUsuario(self, nombre, apellido, username, email, password, roles):

        usuario = Usuario(nombre, apellido, username, email, password)
        self.ses.add(usuario)
        self.ses.commit()
        if type(roles) == list:
            for id in roles:
                relacion = UsersRoles(usuario.id, id)
                self.ses.add(relacion)
        else:
            relacion = UsersRoles(usuario.id, roles)
            self.ses.add(relacion)
        self.ses.commit()
        print type(roles)
    
    def crearRol(self, nombre, descripcion, permisos):
    
        rol = Role(nombre, descripcion)
        self.ses.add(rol)
        self.ses.commit()
        if type(permisos) == list:
            for id in permisos:
                relacion = RolesPermissions(rol.id, id)
                self.ses.add(relacion)
        else:
            relacion = RolesPermissions(rol.id, permisos)
            self.ses.add(relacion)
        self.ses.commit()
    
    def crearPermiso(self, nombre, descripcion):
        permiso = Permission(nombre, descripcion)
        self.ses.add(permiso)
        self.ses.commit()


    

    def eliminar(self, modulo, id):
        """
        Elimina un registro de la base de datos.

        Recibe como parámetro el nmbre del módulo del cual se está accediendo.

        Retorna un mesaje con el estado de la transacción.
        """
        if modulo == "permisos":
            instancia = self.ses.query(Permission).filter_by(id=id).first()
        elif modulo == "roles":
            instancia = self.ses.query(Role).filter_by(id=id).first()
        elif modulo == "usuarios":
            instancia = self.ses.query(Usuario).filter_by(id=id).first()
        retorno = "El registro %s fué eliminado" % id
        try:
            self.ses.delete(instancia)
            self.ses.commit()
        except Exception, e:
            retorno = "Ha ocurrido un error al intentar eliminar:", e
        return retorno

    def update(self, id,diccionario):
        instancia = None
        modulo = "usuarios"
        if modulo == "permisos":
            instancia = self.ses.query(Permission).filter_by(id=id).first()
        elif modulo == "roles":
            instancia = self.ses.query(Role).filter_by(id=id).first()
        elif modulo == "usuarios":
            instancia = self.ses.query(Usuario).filter_by(id=id).first()
        retorno = "El registro %s fué actualizado" % id
        instancia.update(diccionario)
        self.ses.add(instancia)
        self.ses.commit()
#        except Exception, e:
#            retorno = "Ha ocurrido un error al intentar eliminar:", e
        return retorno
       
       
       
    def obtenerDatosJson(self, tabla):
        """
        Devuelve los datos de una tabla por medio de un diccionario.

        Recibe como parámetro el nombre de la tabla a la cual acceder.

        Retorna un diccionario de diccionarios cada uno lleno con conjuntos clave-valor
        que hacen referencia a los atributos de los objetos dto propios de la
        consulta y con clave igual al id de objeto.
        """
        diccionario = {}
        consulta = None
        if tabla.lower() == "users":
            consulta = self.ses.query(Usuario)
        elif tabla.lower() == "permissions":
            consulta = self.ses.query(Permission)
        elif tabla.lower() == "roles":
            consulta = self.ses.query(Role)
        for instancia in consulta:
            dicTemp = instancia.toDict()
            id=dicTemp["id"]
            del dicTemp["id"]
            diccionario[id]=dicTemp
        return diccionario

if __name__ == "__main__":
    dbmm = DatabaseManager()
    hola=json.dumps(dbmm.obtenerDatosJson("roles"),ensure_ascii=False).encode("utf-8")
    
    print hola
    
    