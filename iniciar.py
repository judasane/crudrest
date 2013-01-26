# -*- coding: utf-8 -*-
import cherrypy
import indice
#Cambio el puerto y set de caracteres por defecto de la aplicacion

#cherrypy.config.update({
#    'tools.staticdir.root:':'E:\Juan\Dropbox\Capacitacion\Python\WeBD\recursos',
#    'tools.staticdir.on' : True,
#    'tools.staticdir.dir': "recursos",
    
  #  })
cherrypy.config.update("configuracion.conf")


sitio = indice.SitioWeb()

cherrypy.quickstart(sitio)
