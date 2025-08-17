"""1)"""
print("Hola Mundo!")

"""2) """
nombre = input("Por favor, ingrese su nombre: ")
print(f"¡Hola {nombre}!")

"""3)"""
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_residencia = input("Por favor, ingrese su lugar de residencia: ") 
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

"""4)""" 
radio = float(input("Por favor, ingrese el radio del círculo: "))
perimetro = 3.14159 * radio * 2
area = 3.14159 * (radio ** 2)
print(f"el circulo tiene como perimetro {perimetro} y el área es: {area}")

"""5)"""
segundos = int(input("Por favor, ingrese una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_diferencia = segundos % 60
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_diferencia} segundos.")

"""6)"""  
numero= int(input("Por favor, ingrese un numero para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

"""7)""" 
numero1 = int(input("Por favor, ingrese el primer número entero distinto de 0: "))
numero2 = int(input("Por favor, ingrese el segundo número entero distinto de 0: ")) 
if numero1 != 0 and numero2 != 0: """comprobar que el numero2 no sea 0"""    
suma = numero1 + numero2
division = numero1 // numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2
print(f"Resultados: Suma: {suma}, División: {division}, Multiplicación: {multiplicacion}, Resta: {resta}")

"""8)"""
altura = float(input("Por favor, ingrese su altura: "))
peso = float(input("Por favor, ingrese su peso: "))
imc = peso / (altura **2)
print(f"Su índice de masa corporal es: {imc}")

"""9)"""

celsius = float(input("Por favor, ingrese una temperatura actual en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} grados Celsius equivalenes igual a {fahrenheit} grados Fahrenheit.") 

"""10)""" 
numero1 = float(input("Por favor, ingrese el primer número: "))
numero2 = float(input("Por favor, ingrese el segundo número: "))
numero3 = float(input("Por favor, ingrese el tercer número: "))
suma = (numero1 + numero2 + numero3)
promedio = suma / 3
print(f"El promedio de los números ingresados es: {promedio}")