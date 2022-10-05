##para instalar panda ejecutar el comando pip install panda

from numpy import short
import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

#print(tablaEmpleados.to_string())

#filtro quiero tener todos los datos de los analistas 1

'''
tablaAndes=tablaSiembras[tablaSiembras["Ciudad"]=="Andes"].head(50)
archivoHTML=tablaAndes.to_html()

archivoTEXTO=open("TablaAndes.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
tablaBarbosa=tablaSiembras[tablaSiembras["Ciudad"]=="Barbosa"].head(50)
archivoHTML=tablaBarbosa.to_html()

archivoTEXTO=open("TablaBarbosa.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
tablaCaldas=tablaSiembras[tablaSiembras["Ciudad"]=="Caldas"].head(50)
archivoHTML=tablaCaldas.to_html()

archivoTEXTO=open("TablaCaldas.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
tablaTamesis=tablaSiembras[tablaSiembras["Ciudad"]=="Támesis"].head(50)
archivoHTML=tablaTamesis.to_html()

archivoTEXTO=open("TablaTamesis.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
tablaYarumal=tablaSiembras[tablaSiembras["Ciudad"]=="Yarumal"].head(50)
archivoHTML=tablaYarumal.to_html()

archivoTEXTO=open("tablaYarumal.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
tablaMedellin=tablaSiembras[tablaSiembras["Ciudad"]=="Medellín"]
datosMedellin=tablaMedellin.sort_values(by="Arboles",ascending=False)
archivoHTML=datosMedellin.to_html()

archivoTEXTO=open("datosMedellin.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
tablaCaucasia=tablaSiembras[tablaSiembras["Ciudad"]=="Caucasia"]
archivoHTML=tablaCaucasia.to_html()

archivoTEXTO=open("tablaCaucasia.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
TablaSantafe=tablaSiembras[(tablaSiembras["Ciudad"]=="Santa Fe de Antioquia")&(tablaSiembras["Arboles"]>250)]
archivoHTML=TablaSantafe.to_html()

archivoTEXTO=open("tablaSantafe.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
tablaCaucasia=tablaSiembras[tablaSiembras["Ciudad"]=="Caucasia"]
suma=tablaCaucasia.groupby("Ciudad")[["Hectareas", "Arboles"]].sum()
archivoHTML=suma.to_html()

archivoTEXTO=open("suma.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
Veredas=tablaSiembras[(tablaSiembras["Vereda"]=="Rio Arriba")|(tablaSiembras["Vereda"]=="La Salazar")]
archivoHTML=Veredas.to_html()

archivoTEXTO=open("Veredas.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''
'''
Veredas=tablaSiembras[(tablaSiembras["Vereda"]=="Rio Arriba")|(tablaSiembras["Vereda"]=="La Salazar")]
archivoHTML=Veredas.to_html()

archivoTEXTO=open("Veredas.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

'''
Quitasol=tablaSiembras[(tablaSiembras["Vereda"]=="Quitasol")]
Quitasol=Quitasol.sort_values(by='Hectareas')
Quitasolprom=Quitasol.groupby("Vereda")[["Hectareas", "Arboles"]].mean()


archivoHTML=Quitasolprom.to_html()

archivoTEXTO=open("Quitasolprom.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

Caramanta=tablaSiembras[(tablaSiembras["Vereda"]=="Caramanta")]
Caramantades=Caramanta.describe()
archivoHTML=Caramantades.to_html()

archivoTEXTO=open("Caramanta.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()