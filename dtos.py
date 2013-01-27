# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

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