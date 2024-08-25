import numpy as np
arr = np.arange(0, 11)
print(arr)
trozo_de_arr = arr[0:6]
print(arr)
#A todo el arreglo le quieto qutar todos los valores y dejarlos
trozo_de_arr[:]=0
#Si ahora imprimimos el array completo, veras que todos los valores han sido
print(arr)
#para solucioar esto utilizaremos el comando copy
arr_copy = arr.copy()
arr_copy[:] = 100
#no obstante la lista original es respetada
print(arr)
