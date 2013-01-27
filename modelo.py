

def GET(entidad):
    """Devuelve un objeto Json con objetos del tipo de la entidad"""
    
    
    
    dic={}
    lista=[]
    retorno=""
    dicTablas={"usuarios":"users","roles":"roles","permisos":"permissions"}
    
    if modulo=="usuarios".lower():
        lista=["ID","Nombre","Apellido","Username","Email"]
    elif modulo=="roles".lower():
        lista=["ID","Nombre","Descripcion"]
    elif modulo=="permisos".lower():
        lista=["ID","Nombre","Descripcion"]
        
    dic["tabla"]=genHtml.llenarTablaBD(dicTablas[modulo],lista,True)
    
    retorno=templater.llenarPlantilla("general/listar", dic)
    return retorno
    
    