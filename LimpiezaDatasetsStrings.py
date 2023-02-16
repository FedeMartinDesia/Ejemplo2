
import pandas as pd

#manejo de strings dentro de columnas

#importando dataset

alumnos_df =pd.read_excel("C:\\Users\\PC\\Documents\\DataScience\\Basico\\Datasets\\Alumnos.xlsx")

#print(alumnos_df)


#el problema en este dataset es que el nombre y el apellido estan en la misma columna
#queremos separarlos
#usaremos el accesor str como puente a que nos deje usar funciones de texto
#a pesar de que un dataframe no las puede usar,y asi poder aplicarlas con method chaining
#split llevara como parametro el caracter que se usara para la separacion

alumnos_df[['nombre','apellido']] = alumnos_df['nombre'].str.split('.',expand=True)

## reordenar las columnas es cuestion de "filtrar" el dataset
## pero poniendo TODAS las columnas que existen en una lista
## en el orden que queremos.
alumnos_df = alumnos_df[['nombre', 'apellido','barrio','promedio']]

##eliminar duplicados
alumnos_df=alumnos_df.drop_duplicates()

alumnos_df['nombre'] = alumnos_df['nombre'].str.title()
alumnos_df['apellido'] = alumnos_df['apellido'].str.title()


print(alumnos_df)

alumnos_df.to_excel("C:\\Users\\PC\\Documents\\DataScience\\Basico\\Datasets\\AlumnosRESULTADO.xlsx")