# -*- coding: utf-8 -*-
from database import DatabaseManager
import json

def getLista(entidad):
    """Devuelve un objeto Json con objetos del tipo de la entidad"""
    dbmm = DatabaseManager()
    return '{"valores":'+json.dumps(dbmm.obtenerDatosJson(entidad),ensure_ascii=False).encode("utf-8")+"}"
    
   
    
if __name__ == "__main__":
    print str(getLista("users"))
    
    