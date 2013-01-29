# -*- coding: utf-8 -*-
import cherrypy
from inicio import Inicio
import os
from indice import SitioWeb

#Cambio el puerto y set de caracteres por defecto de la aplicacion
cherrypy.config.update("configuracion.conf")


inicio = Inicio()
#inicio=SitioWeb()

cherrypy.quickstart(inicio)

