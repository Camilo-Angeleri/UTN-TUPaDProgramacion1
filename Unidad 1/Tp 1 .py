# UTN-TUPaDProgramacion1
#Trabajo practico n1

# ejercicio nº1
print("Hola Mundo!")

# ejercicio nº2
nombre= input("ingresa tu nombre")
print(f"hola "+ nombre)

# ejercicio nº3
nombre= input("ingrese su nombre")
apellido= input("ingrese su apellido")
edad= int(input("ingrese su edad"))
residencia= input("donde reside")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

# ejercicio nº4
radio= int(input("ingrese el radio de un circulo"))
pi= 3.14159
perimetro= (2*pi*radio)
area= (pi*radio**2)
print(f"El Area del circulo es de {area} y el perimetro es de {perimetro} ")

# ejercicio nº5
minutos= int(input("ingrese cuantos minutos quiere calcular"))
hora= (minutos / 60)
print(f"{minutos} minutos equivale a {hora} horas")

# ejercicio nº6
num= float(input("ingrese el numero del cual desea saber su tabla de multiplicar"))
x1= num*1
x2=num*2
x3=num*3
x4=num*4
x5=num*5
x6=num*6
x7=num*7
x8=num*8
x9=num*9
x10=num*10
print(f"su tabla de multiplicar es de {x1}, {x2}, {x3}, {x4}, {x5}, {x6}, {x7}, {x8}, {x9}, {x10}")


# ejercicio nº7
num1= int(input("ingrese el primer numero"))
num2= int(input("ingrese el segundo numero"))
suma= num1 + num2 
resta= num1 - num2
multiplicacion= num1 * num2
division= num1 / num2
print(f"La suma entre {num1} y {num2} es de {suma}")
print(f"La resta entre {num1} y {num2} es de {resta}")
print(f"La multiplicacion entre {num1} y {num2} es de {multiplicacion}")
print(f"La division entre {num1} y {num2} es de {division}")

# ejercicio nº8
peso= float(input("ingrese su peso en Kg"))
altura= float(input("ingrese su altura en Mts"))
IMC= peso / altura ** 2
print(f"Su indice corporal es de {IMC}")

# ejercicio nº9
tempC= float(input("ingrese una temperatura en ºC"))
tempF= 9/5 * tempC + 32
print(f" {tempC}ºC son {tempF}ºF ")

# ejercicio nº10
num1=float(input("ingrese el primer numero"))
num2=float(input("ingrese el segundo numero"))
num3=float(input("ingrese el tercer numero"))
prom= (num1+num2+num3) / 3
print(f"Su promedio es de {prom}")