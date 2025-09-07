"""1""" 
# se crea un programa de imprime numero desde 0 hasta 100
for numero in range(101):
    print(numero) 

"""2""" 
#se crea un programa que pida un numero entero
numero= int(input("ingrese un numero: "))
# se crea un contador para contar los digitos 
contador=0
# ciclo while para contar los digitos del numero
while numero>0:
    numero=numero//10 # division entera
    contador+=1 
print("El numero tiene",contador,"digitos")

"""3""" 
# se pide al usuario que ingrese dos numeros
num1=int(input("ingrese el primer numero: "))  
num2=int(input("ingrese el segundo numero: "))
# se inicializa la variable suma en 0
suma=0
# se verifica que num1 sea menor que num2, si no lo es se intercambian
# se realiza porque si ponia mayor primero no funcionaba el rango
if num1 > num2:
    num1, num2 = num2, num1
# se crea un ciclo for para sumar los numeros entre num1 y num2
for numero in range(num1+1,num2):
    suma+= numero
print("La suma de los numeros entre",num1,"y",num2,"es:",suma)

"""4"""
# se inicializa la variable suma en 0
suma=0  
# se crea un ciclo while para pedir numeros al usuario
while True:
    numero=int(input("ingrese un numero (0 para salir): "))
    if numero==0:  # si el usuario ingresa 0 se sale del ciclo
        break # se rompe el ciclo
    suma+=numero  # se suma el numero ingresado a la variable suma  
print("La suma total es:",suma)

"""5"""
# se importa la libreria random para generar numeros aleatorios
import random   
# se genera un numero aleatorio entre 0 y 9
numero_aleatorio=random.randint(0,9)
# se inicializa la variable intentos en 0
intentos=0
# se crea un ciclo while para pedir numeros al usuario hasta que acierte
while True:
    numero=int(input("Adivina el numero (entre 0 y 9): "))
    intentos+=1  # se incrementa la variable intentos en 1
    if numero==numero_aleatorio:  # si el usuario acierta se sale del ciclo
        break  # se rompe el ciclo  
print("Felicidades! Adivinaste el numero en",intentos,"intentos.")

"""6"""
# se crea un programa de imprime numero desde 100 hasta 0 de forma decreciente
for numero in range(100,0 ,-2):# se usa un paso de -2 para decrementar de 2 en 2
    print(numero) 


"""7"""
# se pide al usuario que ingrese dos numeros
num1=0  
num2=int(input("ingrese un numero entero positivo: "))
# se inicializa la variable suma en 0
suma=0

# se crea un ciclo for para sumar los numeros entre num1 y num2
for numero in range(num1,num2+1): # se usa num2+1 para incluir el numero ingresado por el usuario
    suma+= numero
print("La suma de los numeros entre",num1,"y",num2,"es:",suma)

"""8"""
# se inicializan las variables contadores en 0
pares=0  
impares=0   
positivos=0  
negativos=0 
# se crea un ciclo for para pedir 100 numeros al usuario
for i in range(100):
    numero=int(input("ingrese un numero entero: "))
    if numero%2==0:  # si el numero es par se incrementa el contador de pares
        pares+=1  
    else:  # si el numero es impar se incrementa el contador de impares
        impares+=1  
    if numero>0:  # si el numero es positivo se incrementa el contador de positivos
        positivos+=1  
    elif numero<0:  # si el numero es negativo se incrementa el contador de negativos
        negativos+=1

print("Cantidad de numeros pares:",pares)   
print("Cantidad de numeros impares:",impares)
print("Cantidad de numeros positivos:",positivos)
print("Cantidad de numeros negativos:",negativos)

"""9"""
# se inicializan las variables suma y contador en 0
suma=0  
contador=0
# se crea un ciclo for para pedir 100 numeros al usuario
for i in range(100):
    numero=int(input("ingrese un numero entero: "))
    suma+=numero  # se suma el numero ingresado a la variable suma
    contador+=1  # se incrementa el contador en 1   
media=suma/contador  # se calcula la media
print("La media de los numeros ingresados es:",media)

"""10"""
# se pide al usuario que ingrese un numero entero
numero=int(input("ingrese un numero entero: ")) 
# se inicializa la variable invertido en 0
invertido=0
# se crea un ciclo while para invertir el numero
while numero>0:
    digito=numero%10  # se obtiene el ultimo digito del numero
    invertido=invertido*10+digito  # se agrega el digito al numero invertido
    numero=numero//10  # se elimina el ultimo digito del numero 
print("El numero invertido es:",invertido)
