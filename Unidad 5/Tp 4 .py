# Ejercicio Nº1
Notas= [10,6,8,9,8,1,4,2,6,10] 
print ("Notas de los estudiantes:",Notas)

prom= sum(Notas) / len(Notas)
print(f"El promedio de notas de los estudiantes es:", round(prom,2))

Nota_maxima= max(Notas)
Nota_minima=min(Notas)

print("La nota mas baja es:",Nota_minima)
print("La nota mas alta es:",Nota_maxima)

# Ejercicio Nº2
print("Por favor, Ingrese 5 productos")

productos= []

for i in range(5):
    producto= input(f"producto #{i+1}:")
    productos.append(producto)

productos_ordenados= sorted(productos)
print("La lista de los productos (ordenados alfabeticamente) es:")
for p in productos_ordenados:
    print(f">{p}")

producto_elim= input("Que producto deseas eliminar de la lista?")

if producto_elim in productos:
    productos.remove(producto_elim)
    print(F"El producto {producto_elim} ha sido eliminado")
    print("La nueva lista de productos es:", productos)
else:
    print(f"{producto_elim} no se puede encontrar en la lista.")
    print(f"No se ha Eliminado nada")

# Ejercicio Nº3
import random
numeros_aleatorios=[random.randint(1, 100) for i in range(15)]
print("Lista de numeros generados:",numeros_aleatorios)

pares= []
impares= []

for numero in numeros_aleatorios:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append (numero)

print("Numeros pares encontrados:", pares)
print("Numeros impares encontrados:", impares)

# Ejercicio Nº4

# Ejercicio Nº5

# Ejercicio Nº6

# Ejercicio Nº7

# Ejercicio Nº8

# Ejercicio Nº9

# Ejercicio Nº10