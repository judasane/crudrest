# -*- coding: utf-8 -*-
import cherrypy
from cherrypy.lib.cptools import accept
import modelo
import templater

class Inicio:
    "Clase que contiene los metodos principales para mostrar en el sitio web"
    
    @cherrypy.expose
    def index(self,entidad="nalada"):
        methods = ('OPTIONS','GET','POST','PUT','DELETE')
        
        method=cherrypy.request.method
        
        if method not in methods:
            raise cherrypy.HTTPError(400,'Bad Request')
            
        best = accept(['text/html', 'application/json','text/json'])
        
        respuesta=""
        
        if best=="text/html":
            respuesta= self.html(entidad)
            
        else:
            cherrypy.response.headers['Content-Type'] = 'application/json;charset=utf-8'
            respuesta= self.json(entidad)
            print entidad
        
        
        
        return respuesta
            
            
            
    def json(self,entidad):
        return modelo.getLista(entidad)
    
    
    def html(self,entidad):
        return templater.leerArchivo("pruebajax")
    
    
    if __name__ == "__main__":
        
       print modelo.getLista("roles")
            

