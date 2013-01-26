# -*- coding: utf-8 -*-
import os
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Usuario(Base):
    "Inicializa el objeto Usuario con los datos pertinentes"
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    username = Column(String(50))
    email = Column(String(150))
    password = Column(String(32))

    def __init__(self, nombre, apellido, username, email, password):
                
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.email = email
        self.password = password
    def toDict(self):
        dic = {}
        dic["id"] = self.id
        dic["nombre"] = self.nombre
        dic["apellido"] = self.apellido
        dic["username"] = self.username
        dic["email"] = self.email
        dic["password"] = self.password
        return dic
    #  def __repr__(self):
	#	return "ID: %s\nNombre: %s \nApellido: %s\n Username: %s\nPassword: %s\nEmail: %s\n\n" % (self.id,self.nombre,self.apellido,self.username,self.password,self.email)

    def update(self, diccionario):
        """
        Actualiza el usuario a partir de un diccionario de registros de la forma
        atributo:valor
        """
        for propiedad, valor in diccionario.iteritems():
            if propiedad == "nombre":
                self.nombre = valor
            elif propiedad == "apellido":
                self.apellido = valor
            elif propiedad == "username":
                self.username = valor
            elif propiedad == "email":
                self.email = valor
            elif propiedad == "password":
                self.password = valor
        return "exito"

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String)

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def toDict(self):
        dic = {}
        dic["id"] = self.id
        dic["nombre"] = self.nombre
        dic["descripcion"] = self.descripcion
        return dic
        
class Permission(Base):
    __tablename__ = 'Permissions'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String)

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def toDict(self):
        dic = {}
        dic["id"] = self.id
        dic["nombre"] = self.nombre
        dic["descripcion"] = self.descripcion
        return dic
        
class RolesPermissions(Base):
    __tablename__ = "roles_permissions"
    id_role = Column(Integer, primary_key=True)
    id_permission = Column(Integer)
    
    def __init__(self, id_role, id_permission):
        self.id_role = id_role
        self.id_permission = id_permission
        
class UsersRoles(Base):
    __tablename__ = "users_roles"
    id_user = Column(Integer, primary_key=True)
    id_role = Column(Integer)
    
    def __init__(self, id_user, id_role):
        self.id_user = id_user
        self.id_role = id_role
       


class DatabaseManager:
    """
    Clase que se encarga de gestionar las comunicaciones con la base de datos.
    
    Recibe como parámetros el esquema y el motor.
    """
    Session = None
    ses = None
    
    def __init__(self, esquema, motor):
        if motor.lower() == "mysql":
			if os.name == "posix":
				clave = "noentrar"
			else:
				clave = ""
			engine = create_engine("mysql://root:" + clave + "@127.0.0.1/" + esquema + "?charset=utf8", echo=False)
        self.Session = sessionmaker(bind=engine)
        self.ses = self.Session()

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
       

if __name__ == "__main__":
    dbmm = DatabaseManager("WeBD", "MySql")
    print dbmm.update(82,{"email":"jochepe@gmail.com","apellido":"cambiado"})
    