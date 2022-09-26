##para instalar panda ejecutar el comando pip install panda

import pandas as pd

tablaEmpleados=pd.read_csv('./empleados.csv')

#print(tablaEmpleados.to_string())

#filtro quiero tener todos los datos de los analistas 1

"""""
tablaAnalistas1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaAnalistas1.to_html()

archivoTEXTO=open("datosanalistas1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
"""
'''
tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaAnalistas2.to_html()

archivoTEXTO=open("datosanalistas2.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

'''

tablasalario=tablaEmpleados[(tablaEmpleados["salario"]>=5000000) & (tablaEmpleados["edad"]<=30)].head(50)
archivoHTML=tablasalario.to_html()

archivoTEXTO=open("tablasalario.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()