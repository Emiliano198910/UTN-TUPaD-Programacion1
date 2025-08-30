"""1"""
# solicitar ingreso de edad
edad = int(input("Ingresa tu edad: "))
# determinar si es mayor o menor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

"""2"""
# solicitar ingreso de nota al usuario
nota= int(input("Ingresa tu nota: "))
# realizar analisis de su estado
if nota >= 6:
    print("Aprobado")  
else:
    print("Desaprobado")

"""3"""
#ingrese un número
numero = int(input("Ingresa un número: "))
#defina si su número es par o impar
if numero % 2 == 0:
    print("Ha ingresado un número par.")    
else:
    print("Por favor, ingrese un número par.")


"""4"""
#solictar ingreso de edad al usuario
edad1 = int(input("Ingrese su edad:"))
#verificar a que grupo pertenece
if edad1 < 12:
    print ("Niños, menor de 12 años")
elif edad1 >= 12 and edad1 < 18:
    print ( "Adolescente, mayor a 12 años y menor a 18 años")
elif edad1 >= 18 and edad1 < 30:
    print ("Adulto, mayor a 18 años y menor a 30 años")
else :
     print ("Adulto mayor, mayor o igual a 30 años")

"""5"""
#introduza una contraseña entre 8 y 14 caracteres
contraseña = input("Ingrese una contraseña:")
#analizar si cumple con la longitud adecuada
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")   
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")   

"""6"""
#se genera programa que tome listados de numeros aleatorios
import random #creo una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range (50)]  
import statistics   #calculo la media, mediana y moda de la lista
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios) 
moda = statistics.mode(numeros_aleatorios)  
print("Media:", media)
print("Mediana:", mediana)  
print("Moda:", moda)
if moda > mediana and mediana > media:
    print("Sesgo positivo") 
elif moda < mediana and mediana < media:
    print("Sesgo negativo")
else:
    print("No hay sesgo")   

"""7"""
#ingresa una frase
frase = input("Ingrese una frase o palabra: ")
#si ingresa terminado con vocal, se añade signo de exclamación
#caso contrario mensaje que igual
if frase[-1] in "aeiou":
    frase += "!"    
    print(frase)
else:
    print(frase)     

"""8"""   
#solicite ingresar un nombre
nombre = input("Ingrese su nombre: ")
# ingrese un número entre 1 y 3
número = int(input("Ingrese un número del 1 al 3: "))
# si ingreso el número 1 covierte en mayuscula, 2 en minuscula
#3 inicial en mayuscula restantes en minusculas
if número == 1: nombre = nombre.upper()
elif número == 2: nombre = nombre.lower()
elif número == 3: nombre = nombre.title()
print(nombre)
"""9"""
#ingrese datos de terremoto
magnitud= int(input ("Ingrese categorias del terremoto según escale de Ritcher "))   
#analizamos magnitud
if magnitud < 3:
    print ("Muy leve")  
elif magnitud >= 3 and magnitud < 4:
    print ("Leve")  
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte")
elif magnitud >= 7 :
    print ("Extremo")

"""10"""
#solicitamos ingreso de hemisferio al usuario
hemisferio = input("Ingrese el hemisferio (Norte/Sur): ")
#determinar epoca del año
estación = input("Ingrese la estación (Verano/Otoño/Invierno/Primavera): ") 
#segun datos ingresados analizar nor o sur y que epoca
#lower convierte a minuscula los datos ingresados
if hemisferio.lower() == "norte":
    if estación.lower() == "verano":
        print("Desde el 21 de junio hasta el 20 de septiembre")
    elif estación.lower() == "otoño":
        print("desde el 21 de septiembre hasta el 20 de diciembre")
    elif estación.lower() == "invierno":
        print("Desde el 21 de diciembre hasta el 20 de marzo")
    elif estación.lower() == "primavera":
        print("Desde el 21 de marzo hasta el 20 de junio")
    else:
        print("Estación no registrada.")
elif hemisferio.lower() == "sur":
    if estación.lower() == "verano":
        print("Desde el 21 de diciembre hasta el 20 de marzo")
    elif estación.lower() == "otoño":
        print("Desde el 21 de marzo hasta el 20 de junio")
    elif estación.lower() == "invierno":
        print("Desde el 21 de junio hasta el 20 de septiembre")
    elif estación.lower() == "primavera":
        print("Desde el 21 de septiembre hasta el 20 de diciembre")
    else:
        print("Estación no registrada.")





