import pandas as pd

tabla=pd.read_csv('./Siembras.csv')

#tabla de estadisticas 
tablaEstadisticas=tabla.describe()
print(tablaEstadisticas)

#solo obtener medias de la tabla estadisticas (solo 1 fila)
tablaMedias=tablaEstadisticas.loc[['mean']]
print(tablaMedias)

#solo obetener los datos de una columna
tablaMediasArboles=tablaMedias["Arboles"].to_frame()
