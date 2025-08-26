# UTN-TUPaDProgramacion1
# Trabajo practico Nº 2

# Ejercicio Nº1
Edad = int(input("Ingrese su Edad: ")) 
if Edad > 18 :  
    print("Eres mayor de Edad")

# Ejercicio N°2
nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio N°3
num1= int(input("Ingrese un numero par "))
ParoImpar = (num1 % 2)
if ParoImpar == 0:
    print("Ha ingresado un numero Par")
else:
    print("Por favor, Ingrese un numero Par")

# Ejercicio N°4
edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Usted es un/a Niño/a")
elif edad >= 12 and edad < 18 :
    print("Usted es un/a Adolescente")
elif edad >= 18 and edad < 30 :
    print("Usted es un/a Adulto/a joven")
elif edad >= 30 :
    print("Usted es un/a Adulto/a")

# Ejercicio N°5
contraseña = input("Ingrese un contraseña de entre 8 y 14 caracteres")
longtext = len(contraseña)
if longtext >= 8 and longtext <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, Ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio N°6
import random
nums = [random . randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
lista = (nums)
mediaN = mean(lista)
ModoN = mode(lista)
MedianaN = median(lista)
print(lista)
print(mediaN)
print(MedianaN)
print(ModoN)
if mediaN > MedianaN and MedianaN > ModoN:
    print("Hay Sesgo positivo o a la derecha")
elif mediaN < MedianaN and MedianaN< ModoN:
    print("Hay Sesgo negativo o a la izquierda")
elif mediaN == MedianaN and MedianaN == ModoN and ModoN == mediaN:
    print("Sin Sesgo")

# Ejercicio N°7

# Ejercicio N°8

# Ejercicio N°9

# Ejercicio N°10