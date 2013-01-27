# -*- coding: utf-8 -*-
import cherrypy
import indice
import os

#Cambio el puerto y set de caracteres por defecto de la aplicacion
cherrypy.config.update("configuracion.conf")


sitio = indice.SitioWeb()

cherrypy.quickstart(sitio)

#Esto es un comentario

    