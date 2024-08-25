import numpy as np
#Definamos un numero del 1 al 20 en un vector
arr = np.random.randint(1,20,10)
#print(arr)
#ahora creamos una estructura matricial
matriz =arr.reshape(2,5)
print(matriz)
#max vamos a traer el número máximo que tenga nuestro arreglo
maximo = matriz.max()
print(maximo)
#Creamos un array de dos dimensiones
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
print(a)
#qye oasa cyabdi quieres unir el array b con el array a
#con el comando concatenate se unen
c= np.concatenate((a,b), axis =0)
print(c)
