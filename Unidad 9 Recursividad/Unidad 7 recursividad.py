"""1"""
def factorial(n): # Función recursiva para calcular el factorial
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # Llamada recursiva
numero = int(input("Ingrese un número entero positivo: "))
for i in range(1, numero + 1): # Iterar desde 1 hasta el número ingresado
    print(f"El factorial de {i} es {factorial(i)}")     

"""2"""
def fibonacci(n): # Función recursiva para calcular número de Fibonacci
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Llamada recursiva
posicion = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")    
for i in range(posicion):
    print(fibonacci(i), end=" ")    

"""3"""

def potencia(base, exponente): # Función recursiva para calcular la potencia
    if exponente == 0: 
        return 1
    else:
        return base * potencia(base, exponente - 1) # Llamada recursiva
base = float(input("Ingrese la base: ")) 
exponente = int(input("Ingrese el exponente (entero no negativo): "))   
resultado = potencia(base, exponente) # Calcular la potencia
print(f"{base} elevado a la {exponente} es {resultado}")

"""4"""
def decimal_a_binario(n): # Función recursiva para convertir decimal a binario
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2) # Llamada recursiva
numero_decimal = int(input("Ingrese un número entero positivo en base decimal: "))
binario = decimal_a_binario(numero_decimal) # Convertir a binario
if binario == "":
    binario = "0"
print(f"La representación binaria de {numero_decimal} es: {binario}")

"""5"""
def es_palindromo(palabra): # Función recursiva para verificar si una palabra es palíndromo
    if len(palabra) <= 1: 
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1]) # Llamada recursiva
palabra = input("Ingrese una palabra sin espacios ni tildes: ")
if es_palindromo(palabra): # Verificar si es palíndromo
    print(f"La palabra '{palabra}' es un palíndromo.")
else: # No es palíndromo
    print(f"La palabra '{palabra}' no es un palíndromo.")


"""6"""
def suma_digitos(n): # Función recursiva para sumar los dígitos de un número
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10) # Llamada recursiva
numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)    # Sumar los dígitos
print(f"La suma de los dígitos de {numero} es: {resultado}")

"""7"""
def contar_bloques(n): # Función recursiva para contar bloques en una pirámide
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1) # Llamada recursiva
nivel_inferior = int(input("Ingrese el número de bloques en el nivel más bajo: "))
total_bloques = contar_bloques(nivel_inferior) # Contar bloques totales
print(f"El total de bloques necesarios para construir la pirámide es: {total_bloques}")

"""8"""
def contar_digito(numero, digito): # Función recursiva para contar apariciones de un dígito
    if numero == 0:
        return 0
    else:
        cuenta = 1  if numero % 10 == digito else 0 # Verificar el dígito actual
        return cuenta + contar_digito(numero // 10, digito) # Llamada recursiva
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (entre 0 y 9): "))
veces = contar_digito(numero, digito) # Contar apariciones del dígito
print(f"El dígito {digito} aparece {veces} veces en el número {numero}.")
