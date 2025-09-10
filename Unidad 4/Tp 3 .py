# Ejercicio Nº1
for i in range(101):
    print(i)

# Ejercicio Nº2
num = int(input("Ingrese un numero entero"))

if num > 0  :
    cont = 0
    while num > 0 :
        num //= 10
        cont += 1
        digitos = cont
elif num < 0:
    num = -num
    while num > 0 :
        num //= 10
        cont += 1
        digitos = cont
elif num == 0:
    digitos = 1
else:
    print("Por favor, ingrese un numero entero")

print(f"El numero ingresado tiene {digitos} digitos")

# Ejercicio Nº3
num1 = int(input("Ingrese un numero entero"))
num2 = int(input("Ingrese un numero entero"))
sumatoria = 0

if num1 > num2 :
    for i in range((num2)+1 ,num1):
     sumatoria += i 
    print(f"la sumatoria de los numeros intermedios es ",sumatoria)
else:
    for i in range((num1)+1,num2):
     sumatoria += i
    print(f"la sumatoria de los numeros intermedios es",sumatoria)

# Ejercicio Nº4
corte = 0
sumatoria = 0

while corte == 0:
    num = int(input("Ingrese un numero"))
    sumatoria += num
    if num == 0 :
        corte += 1

print(f"La sumatoria de los numero ingresados es", sumatoria)

# Ejercicio Nº5
import random
numero_random = random.randint(0 , 9)
cont = 0

while num != numero_random:
    num = int(input("Ingrese un numero entre el 0 y el 9"))
    cont += 1

print("Correcto")
print(f"Lo adivinaste en {cont} intentos")

# Ejercicio Nº6
for i in range (-100, 1, 2):
    print(-i)

# Ejercicio Nº7
num = int(input("Ingrese un numero positivo"))
sumatoria = 0

if num > 0 :
    for i in range(0,num):
        sumatoria += i
    print(f"La sumatoria de los numero entre el 0 y {num} es de {sumatoria}")
else:
    print("Por favor ingrese un numero positivo")

# Ejercicio Nº8
cont_pares = 0
cont_impares = 0
cont_pos = 0
cont_neg = 0

for i in range(100):
    num = int(input("Ingrese un numero entero"))
    print(num)

    if num % 2 == 0:
        cont_pares += 1
    elif num % 2 != 0:
        cont_impares += 1
    if num > 0:
        cont_pos += 1
    elif num < 0:
        cont_neg += 1
    

print(f"Cantidad de numeros pares {cont_pares}")
print(f"Cantidad de numeros impares {cont_impares}")
print(f"Cantidad de numeros positivos {cont_pos}")
print(f"Cantidad de numeros negativos {cont_neg}")

# Ejercicio Nº9
sumatoria = 0

for i in range(100):
    num = int(input("Ingrese un numero entero"))
    sumatoria += num
    print(num)

print(f"La media de los numeros ingresados es de",sumatoria / 100)

# Ejercicio Nº10
numero_original =int(input("Ingrese un numero "))
num = numero_original
num_inv = 0

while num > 0:
    ult_digito = num % 10
    num_inv = num_inv * 10 + ult_digito
    num = num // 10

print(numero_original)
print(f"Y sus digitos inveros son: {num_inv}")