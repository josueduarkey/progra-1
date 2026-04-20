import numpy as np

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

zeros = np.zeros(5)
print(zeros)

ones = np.ones(5)
print(ones)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
# SUMA
result = arr1 + arr2
print(result)
# MULTIPLICACION
resultado = arr1 * arr2
print(resultado)

arr3 = np.array([1, 2, 3])
result1 = arr3 + 5
print(result1)

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2


arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
print(slice)
# Recupera los elementos 2, 3 y 4
# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
# Recupera los elementos donde la condición es verdadera: [3, 4, 5]
print(result)

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices]
print(result)
# Recupera los elementos en los índices especificados: [1, 3, 5]

#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales


consumo = np.array([
 [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
 [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
 [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
 [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
 [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
 [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
 [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
 [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
 [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
 [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])


print("Dimensiones: ", consumo.ndim)
print("Forma", consumo.shape)
print("Consumo primero hogar: ", consumo[0])
print("Consumo el miércoles de (día 3): ", consumo[:, 2])

promedio_por_hogar = np.mean(consumo, axis = 1)
promedio_por_dia = np.mean(consumo, axis = 0)
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)


# Máximos por hogar
maximos = np.max(consumo, axis = 1)
# Minimos por hogar
minimos = np.min(consumo, axis = 0)
# Desviación estandar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

# Suma por hogar (Semana)
consumo_total_hogar = np.sum(consumo, axis = 1)
# Indice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# Indice del hogar con menor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)


print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)


consumo_total_hogar = np.sum(consumo, axis = 1)
print(f'Consumo total de cada hogar durante la semana: {consumo_total_hogar}')

# Comparar cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100

consumo_mayor_100 = np.where(altos)[0]

print(f'Id de hogares con consumos  mayor a 100: {consumo_mayor_100}')

consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# Resultado 
print(consumo_normalizado)

# RESPUESTAS DEL CUESTIONARIO
'''
1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
'''
consumo_hogar_5 = np.array(consumo[4,4])
print(f'El consumo del hogar 5 el viernes (día 5) {consumo_hogar_5}')

''' 
2. Usando indexación, muestra el consumo de los 
últimos 3 hogares el domingo
'''
consumo_hogar_domingo = np.array(consumo[], axis = 0)