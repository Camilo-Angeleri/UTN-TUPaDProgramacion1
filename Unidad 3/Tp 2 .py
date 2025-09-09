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
palabra = input("Ingrese una palabra")
ultima_letra = palabra [-1]
if ultima_letra == "a" or ultima_letra == "A":
    print(f"{palabra}!")
elif ultima_letra == "e" or ultima_letra == "E":
    print(f"{palabra}!")
elif ultima_letra == "i" or ultima_letra == "I": 
    print(f"{palabra}!")
elif ultima_letra == "o" or ultima_letra == "O":
    print(f"{palabra}!")
elif ultima_letra == "u" or ultima_letra == "U":
    print(f"{palabra}!")
else:
    print(f"{palabra}")

# Ejercicio N°8
nombre = input("Ingrese su nombre")
nombre_MAY = nombre.upper()
nombre_MIN = nombre.lower()
nombre_tit = nombre.title()
tipo =int(input("Ingrese que tipo desea "))
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
if tipo == 1:
    print(f"{nombre_MAY}")
elif tipo == 2:
    print(f"{nombre_MIN}")
elif tipo == 3:
    print(f"{nombre_tit}")
else:
    print("Por favor, Ingrese un numero del 1 al 3")

# Ejercicio N°9
magnitud_terremoto = int(input("Por Favor ingrese la magnitud del terremoto"))
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio N°10
hemisferio = input("Ingrese en que hemisferio se encuentra (Norte/Sur)")
mes = int(input("Ingrese el mes (numerico)"))
dia = int(input("Ingrese el dia"))
if dia <= 31 and mes <= 12:
    if hemisferio == "norte":
        if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes == 2 and dia <= 31 ) or (mes == 1 and dia <= 31):
            print("Invierno")
        elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes == 5 and dia <= 31 ) or (mes == 4 and dia <= 31):
            print("Primavera")
        elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes == 8 and dia <= 31 ) or (mes == 7 and dia <= 31):
            print("Verano")
        elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes == 11 and dia <= 31 ) or (mes == 10 and dia <= 31):
            print("Otoño")
    elif hemisferio == "sur":
        if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes == 2 and dia <= 31 ) or (mes == 1 and dia <= 31):
            print("Verano")
        elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes == 5 and dia <= 31 ) or (mes == 4 and dia <= 31):
            print("Otoño")
        elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes == 8 and dia <= 31 ) or (mes == 7 and dia <= 31):
            print("Invierno")
        elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes == 11 and dia <= 31 ) or (mes == 10 and dia <= 31):
            print("Primavera")
    else:
         print("Por favor, Ingrese un Hemisferio")
else:
    print("Fecha Invalida")