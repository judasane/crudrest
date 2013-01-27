# -*- coding: utf-8 -*-
import cherrypy
from cherrypy.lib.cptools import accept

class Inicio:
    "Clase que contiene los metodos principales para mostrar en el sitio web"
    
    @cherrypy.expose
    def index(self,id=None):
        methods = ('OPTIONS','GET','POST','PUT','DELETE')
        
        method=cherrypy.request.method
        
        if method not in methods:
            raise cherrypy.HTTPError(400,'Bad Request, no aceptado')
            
        best = accept(['text/html', 'application/json','text/json'])
        
        respuesta=""
        
        if best=="text/html":
            respuesta= self.html(method)
        else:
            respuesta= self.json(method,id)
        
        return respuesta
            
    def json(self,method,id=None,entidad=None):
        pass
    
    
    def html(self,method):
        pass
    
    
                       
            

