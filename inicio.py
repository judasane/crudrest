# -*- coding: utf-8 -*-
import cherrypy
from cherrypy.lib.cptools import accept
import modelo

class Inicio:
    "Clase que contiene los metodos principales para mostrar en el sitio web"
    
    @cherrypy.expose
    def index(self,entidad="nada"):
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
        
        return respuesta
            
            
            
    def json(self,entidad="permissions"):
        return modelo.GET(entidad)
    
    
    def html(self,entidad):
        return "<h1>Todavía no lo hemos desarrollado, aguante tantico!! %s</h1>" % entidad
    
    
    if __name__ == "__main__":
        
       print modelo.GET("roles")
            

