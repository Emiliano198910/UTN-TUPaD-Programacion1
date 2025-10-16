"""1"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} # Diccionario con precios de frutas
print (precios_frutas)

#agregar elementos
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print (precios_frutas)

"""2"""
#modificar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print (precios_frutas)

"""3"""
precios_frutas.keys() # Obtener las claves del diccionario
print (precios_frutas.keys())

"""4"""
agenda_contactos = {} # Diccionario para almacenar contactos
for _ in range(5): # Solicitar 5 contactos
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda_contactos[nombre] = numero # Agregar al diccionario 
print("Contactos guardados.")
# Consultar un contacto
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in agenda_contactos:
    print(f"El número de {nombre_consulta} es {agenda_contactos[nombre_consulta]}.")
else:
    print(f"No se encontró el contacto {nombre_consulta}.")

"""5"""
frase = input("Ingrese una frase: ")
palabras = frase.split() # Dividir la frase en palabras
palabras_unicas = set(palabras) # Palabras únicas
print("Palabras únicas:", palabras_unicas)  
# Contar la frecuencia de cada palabra
frecuencia_palabras = {}
for palabra in palabras: 
    if palabra in frecuencia_palabras: # Si la palabra ya está en el diccionario
        frecuencia_palabras[palabra] += 1 # Incrementar su contador
    else:
        frecuencia_palabras[palabra] = 1 # Inicializar su contador
print("Frecuencia de palabras:", frecuencia_palabras)

"""6"""
alumnos = {} # Diccionario para almacenar alumnos y sus notas
for _ in range(3): # Solicitar 3 alumnos    
    nombre = input("Ingrese el nombre del alumno: ")
    notas = [] # Lista para almacenar las notas
    for i in range(3): # Solicitar 3 notas
        nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota) # Agregar la nota a la lista
    alumnos[nombre] = tuple(notas) # Almacenar las notas como una tupla en el diccionario   
# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items(): 
    promedio = sum(notas) / len(notas) # Calcular el promedio
    print(f"El promedio de {nombre} es {promedio:.2f}")

"""7"""
parcial1 = {1, 2, 3, 4, 5} # Estudiantes que aprobaron Parcial 1
parcial2 = {4, 5, 6, 7} # Estudiantes que aprobaron Parcial 2
# Estudiantes que aprobaron ambos parciales
aprobados_ambos = parcial1.intersection(parcial2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
# Estudiantes que aprobaron solo uno de los dos parciales
aprobados_solo_uno = parcial1.symmetric_difference(parcial2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
# Lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
aprobados_al_menos_uno = parcial1.union(parcial2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)

# Estudiantes que no aprobaron ninguno de los dos parciales (del 1 al 10)
todos_estudiantes = set(range(1, 11)) # Estudiantes del 1 al 10
no_aprobados = todos_estudiantes - aprobados_al_menos_uno
print("Estudiantes que no aprobaron ninguno de los dos parciales:", no_aprobados)

"""8"""
stock_productos = {} # Diccionario para almacenar productos y su stock
while True:
    accion = input("Ingrese una acción (consultar, agregar, nuevo, salir): ").lower() 
    if accion == "salir": 
        print("Saliendo del programa.")
        break
    elif accion == "consultar": # Consultar el stock de un producto
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock_productos: # Si el producto existe
            print(f"El stock de {producto} es {stock_productos[producto]}.")
        else: # Si el producto no existe
            print(f"El producto {producto} no existe en el stock.")
    elif accion == "agregar": # Agregar unidades al stock de un producto existente
        producto = input("Ingrese el nombre del producto para agregar stock: ")
        if producto in stock_productos: # Si el producto existe
            cantidad = int(input(f"Ingrese la cantidad a agregar al stock de {producto}: "))
            stock_productos[producto] += cantidad # Actualizar el stock
            print(f"Nuevo stock de {producto} es {stock_productos[producto]}.")
        else:
            print(f"El producto {producto} no existe. Use 'nuevo' para agregarlo.")
    elif accion == "nuevo":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock_productos: # Si el producto no existe
            cantidad = int(input(f"Ingrese la cantidad inicial de stock para {producto}: "))
            stock_productos[producto] = cantidad # Agregar el nuevo producto
            print(f"Producto {producto} agregado con un stock de {cantidad}.")
        else:
            print(f"El producto {producto} ya existe. Use 'agregar' para aumentar su stock.")
    else:
        print("Acción no reconocida. Por favor, intente de nuevo.")

"""9"""
agenda = {} # Diccionario para almacenar la agenda
# Agregar eventos a la agenda
for _ in range(3): # Solicitar 3 eventos
    dia = input("Ingrese el día del evento (por ejemplo, 'Lunes'): ")
    hora = input("Ingrese la hora del evento (por ejemplo, '14:00'): ")
    evento = input("Ingrese la descripción del evento: ")
    agenda[(dia, hora)] = evento # Usar una tupla (día, hora) como clave    
# Consultar un evento en la agenda
dia_consulta = input("Ingrese el día para consultar el evento: ")
hora_consulta = input("Ingrese la hora para consultar el evento: ")
clave_consulta = (dia_consulta, hora_consulta)
if clave_consulta in agenda: # Si el evento existe
    print(f"El evento programado para {dia_consulta} a las {hora_consulta} es: {agenda[clave_consulta]}.")
else: # Si no existe
    print(f"No hay ningún evento programado para {dia_consulta} a las {hora_consulta}.")

"""10"""
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'Perú': 'Lima'} # Diccionario original de países y capitales
capitales_paises = {} # Nuevo diccionario invertido
for pais, capital in paises_capitales.items(): 
    capitales_paises[capital] = pais # Invertir clave y valor   
print("Diccionario original (países a capitales):", paises_capitales)
print("Diccionario invertido (capitales a países):", capitales_paises)






