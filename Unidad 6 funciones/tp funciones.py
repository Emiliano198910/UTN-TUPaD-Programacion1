"""1"""
def imprimir_hola_mundo(): # Función para imprimir "Hola Mundo!"
    print("Hola Mundo!")    
imprimir_hola_mundo()   

"""2""" 
def saludar_usuario(): # Solicitar y mostrar el nombre del usuario
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}!")
saludar_usuario()


"""3"""
def informacion_personal(): # Solicitar y mostrar información personal
    nombre= input("Ingrese su nombre: ")
    apellido= input("Ingrese su apellido: ")
    edad= input("Ingrese su edad: ")
    residencia= input("Ingrese su lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
informacion_personal()

"""4"""

import math # Importar la biblioteca matemática para usar pi
def calcular_area_circulo(radio): # Calcular el área del círculo
    area = math.pi * radio ** 2
    return area
def calcular_perimetro_circulo(radio): # Calcular el perímetro del círculo
    perimetro = 2 * math.pi * radio
    return perimetro
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)   
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

"""5"""

def segundos_a_horas(segundos): # Convertir segundos a horas
    horas = segundos / 3600 # 1 hora = 3600 segundos
    return horas
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print( f"los {segundos}segundos es igual a {horas} horas.")

"""6"""
def tabla_multiplicar (numero): # Mostrar la tabla de multiplicar
    for i in range(1, 11): # De 1 a 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

"""7"""

def operaciones_basicas(a,b): # Realizar operaciones básicas
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b # Asumimos que b no es cero
    return (suma, resta, multiplicacion, division)
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número que no sea cero: "))
if b == 0:
        print("El segundo número no puede ser cero para la división.")
        b = float(input("Por favor, ingrese un número diferente de cero: "))
resultados = operaciones_basicas(a,b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

"""8"""

def calcular_imc(peso, altura): # Calcular el Índice de Masa Corporal (IMC)
    imc = peso / (altura ** 2) 
    return imc
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

"""9"""

def celsius_a_fahrenheit(celsius): # Convertir Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"los {celsius} grados Celsius que ingreso son {fahrenheit} grados Fahrenheit.")

"""10"""

def calcular_promedio (a, b, c): 
    promedio = (a + b + c) / 3 # Calcular el promedio
    return promedio
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los 3 números ingresados es: {promedio}")












