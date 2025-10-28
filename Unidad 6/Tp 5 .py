# Ejercicio Nº1
# Definicion de Funcion

def imprimir_HolaMundo():
    print("Hola Mundo!") #Imprime por pantalla el mensaje Hola Mundo!

# Programa Principal

imprimir_HolaMundo()

# Ejercicio Nº2
# Definicion de Funcion
def saludar_usuario():
    nombre= input()
    print(f"Hola {nombre}!")

# Programa Principal

saludar_usuario()

# Ejercicio Nº3
# Definicion de Funcion
def informacion_personal():
    nombre= input("Ingrese su Nombre")
    apellido= input("Ingrese su Apellido")
    edad= input("Ingrese su edad")
    residencia= input("Ingrese su lugar de residencia")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa Principal

informacion_personal()

# Ejercicio Nº4
import math
PI = math.pi
radio= int(input("ingrese el radio del circulo"))

def calcular_area_circulo():
    area= (radio ** 2) * PI
    print(f"El area de un circulo con radio {radio} es igual a {area}")

def calcular_perimetro_circulo():
    perimetro= 2 * PI * radio
    print(f"El perimetro de un circulo con radio {radio} es igual a {perimetro}")

# Programa Principal
calcular_area_circulo()
calcular_perimetro_circulo()

# Ejercicio Nº5

# Ejercicio Nº6

# Ejercicio Nº7

# Ejercicio Nº8

# Ejercicio Nº9

# Ejercicio Nº10