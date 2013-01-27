# -*- coding: utf-8 -*-
import json
diccionarioso=json.loads('{"1":{"nombre":"Juan","apellido":"Sánchez","Username":"Judasane","Email":"judasane@gmail.com"}, "2":{"nombre":"Violeta","apellido":"Sánchez","Username":"VioSaGa","Email":"viosaga@gmail.com"}}')
print type(diccionarioso)
print diccionarioso["2"]["nombre"]

