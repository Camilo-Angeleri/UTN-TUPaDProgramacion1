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
datos = [1,3,5,3,7,1,9,5,3]
print("Lista original:",datos)

datos_set = set(datos)
lista_datos = list(datos_set)

print("Lista de sin datos repetidos:",lista_datos)

# Ejercicio Nº5
estudiantes_ptes = [ "Camilo", "Martina","Claudio", "Ernestina", "Ernesto", "Kyra", "Betiana", "Martin"]
print("listan de estudiantes presentes:",estudiantes_ptes)

accion=input("¿Qué deseas hacer? (escribe 'agregar' para sumar un estudiante o 'eliminar' para quitar uno): ").lower()

if accion == "agregar":
    nuevo_estudiante= input("Ingrese el nombre de estudiante nuevo:")
    estudiantes_ptes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} ha sido agregado.")
elif accion == "eliminar":
    eliminar_estudiante = input("Ingrese el estudiante que desea eliminar:")
    if eliminar_estudiante in estudiantes_ptes:
        estudiantes_ptes.remove(eliminar_estudiante)
        print("Se ha eliminado un Estudiante del listado")
    else:
        print("El estudiante ingresado no se encuentra en el listado")

if accion == "agregar" or accion == "eliminar":
    print("El listado de estudiantes actualizado es:", estudiantes_ptes)
else:
    print("Listado de estudiantes:", estudiantes_ptes)

# Ejercicio Nº6
numeros = [22,44,66,88,00]
print("Listado de Numeros:", numeros)

rotacion_num = [numeros[-1]] + numeros[:-1]
print("Lista rotada:",rotacion_num)

# Ejercicio Nº7
Temperaturas_semana = [[25.3, 28.4],[27.3, 32.4],[26.9, 34.5],[27.3, 32.4],[26.3, 31.8],[20.3, 26.4]]
dia_semana= ["lunes","Martes","Miercoles","jueves","viernes","Sabado","Domingo"]

sum_min= 0
sum_max= 0

for dia in Temperaturas_semana:
    sum_min += dia[0]
    sum_max += dia[1]

promedio_min = sum_min/ len(Temperaturas_semana)
promedio_max = sum_max/ len(Temperaturas_semana)

print(f"El promedio de las temperaturas minimas es:,{promedio_min: .2f}°C")
print(f"El promedio de las temperaturas maximas es:,{promedio_max: .2f}°C")

mayor_amplitud = -1
dia_mayoramplitud = ""

for i, (min_temp, max_temp) in enumerate(Temperaturas_semana):
    amplitud_dia = max_temp - min_temp

    if amplitud_dia > mayor_amplitud:
        mayor_amplitud = amplitud_dia
        dia_mayoramplitud = dia_semana[i]

print(F"La mayor amplitud termica se registro el dia {dia_mayoramplitud} con {round(mayor_amplitud,2)}°C ")

# Ejercicio Nº8
notas = [
    [8, 9, 7],  # Notas de Camilo
    [7, 8, 9],  # Notas de Claudio
    [9, 8, 8],  # Notas de Martina
    [6, 7, 7],  # Notas de Betiana 
    [8, 9, 9]   # Notas de Ernestina
]

estudiantes = ["Ana", "Carlos", "Sofía", "David", "Elena"]
materias = ["Matemáticas", "Historia", "Ciencias"]

print("Promedio de cada estudiante:")
for i, estudiante_notas in enumerate(notas):
    promedio_estudiante = sum(estudiante_notas) / len(estudiante_notas)
    print(f"- {estudiantes[i]}: {promedio_estudiante:.2f}")


print("\nPromedio de cada materia:")
for i in range(len(materias)):
    suma_materia = 0
    for j in range(len(estudiantes)):
        suma_materia += notas[j][i]
    promedio_materia = suma_materia / len(estudiantes)
    print(f"- {materias[i]}: {promedio_materia:.2f}")

# Ejercicio Nº9
tablero = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

def mostrar_tablero():
    for fila in tablero:
        print(" | ".join(fila))
    print("-" * 9)

print("¡Comienza el juego de Ta-Te-Ti!")
mostrar_tablero()

for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno de {jugador}")
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingresa la fila (0, 1, 2): "))
            columna = int(input(f"Jugador {jugador}, ingresa la columna (0, 1, 2): "))

            if not (0 <= fila <= 2 and 0 <= columna <= 2):
                print("Error: Coordenadas fuera de rango. Inténtalo de nuevo.")
                continue
            
            if tablero[fila][columna] != '-':
                print("Error: La casilla ya está ocupada. Elige otra.")
                continue

            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
    
    tablero[fila][columna] = jugador

    mostrar_tablero()

print("Fin del juego. Ya no hay más jugadas posibles.")

# Ejercicio Nº10
ventas = [[10, 15, 12, 20, 18, 25, 14],[22, 18, 15, 25, 30, 20, 17],[5, 10, 8, 12, 11, 9, 15],[30, 25, 28, 22, 19, 21, 24]]
productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Total de ventas por producto:")
totales_productos = []

for i, ventas_producto in enumerate(ventas):
    total = sum(ventas_producto)
    totales_productos.append(total)
    print(f"- {productos[i]}: {total} unidades")

totales_por_dia = []

for dia in range(len(dias_semana)):
    total_dia = 0
    for producto in range(len(productos)):
        total_dia += ventas[producto][dia]
    totales_por_dia.append(total_dia)

dia_mas_ventas_index = totales_por_dia.index(max(totales_por_dia))
dia_mas_ventas = dias_semana[dia_mas_ventas_index]
total_dia_mas_ventas = max(totales_por_dia)

print(f"El día con mayores ventas totales fue el {dia_mas_ventas} con {total_dia_mas_ventas} unidades.")