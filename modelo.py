# -*- coding: utf-8 -*-
from database import DatabaseManager
import json

def GET(entidad):
    """Devuelve un objeto Json con objetos del tipo de la entidad"""
    dbman=DatabaseManager()
    #return json.dumps(dbman.obtenerDatosJson(entidad))
    return json.dumps(dbman.obtenerDatosJson(entidad),ensure_ascii=False).encode("utf-8")
   
    
if __name__ == "__main__":
    print str(GET("roles"))
    
    