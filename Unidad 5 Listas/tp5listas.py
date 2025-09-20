"""1"""
def main(): # Función principal
    notas = [] # Lista para almacenar las notas
    for i in range(10):
        while True:
            try:
                nota = float(input(f"Ingrese la nota del estudiante {i + 1} (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota) # Agregar la nota a la lista
                    break
                else:
                    print("Nota inválida. Por favor, ingrese una nota entre 0 y 10.")
            except ValueError: #si ingresa letras en vez de números
                print("Entrada inválida. Por favor, ingrese un número válido.")
    print("Notas ingresadas:", notas) # Mostrar las notas ingresadas 
    promedio = sum(notas) / len(notas) # Calcular el promedio
    print(f"El promedio de las notas es: {promedio:.2f}") 
    nota_mas_alta = max(notas) # Nota más alta
    nota_mas_baja = min(notas)  # Nota más baja 
    print(f"La nota más alta es: {nota_mas_alta}")
    print(f"La nota más baja es: {nota_mas_baja}")  
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal 

"""2"""
def main(): # Función principal
    productos = [] # Lista para almacenar los productos
    for i in range(5):
        producto = input(f"Ingrese el nombre del producto {i + 1}: ")
        productos.append(producto) # Agregar el producto a la lista
    print("Lista de productos ingresados:", productos) 
    productos_ordenados = sorted(productos) # Ordenar la lista alfabéticamente
    print("Lista de productos ordenada alfabéticamente:", productos_ordenados) 
    producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    if producto_a_eliminar in productos:
        productos.remove(producto_a_eliminar) # Eliminar el producto de la lista
        print(f"Producto '{producto_a_eliminar}' eliminado.")
    else:
        print(f"Producto '{producto_a_eliminar}' no encontrado en la lista.")
    print("Lista actualizada de productos:", productos)
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal
"""3"""
import random # Importar el módulo random para generar números aleatorios
def main(): # Función principal 
    numeros = [random.randint(1, 100) for _ in range(15)] # Generar lista de 15 números aleatorios entre 1 y 100
    print("Lista de números generados:", numeros) 
    pares = [num for num in numeros if num % 2 == 0] # Lista de números pares
    impares = [num for num in numeros if num % 2 != 0] # Lista de números impares
    print("Números pares:", pares)
    print("Números impares:", impares)
    print(f"Número de elementos en la lista de pares: {len(pares)}") 
    print(f"Número de elementos en la lista de impares: {len(impares)}")
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal

"""4"""
def main(): # Función principal
    lista_con_repetidos = [1, 3, 5, 3, 7, 1, 9, 5, 3] # Lista con valores repetidos
    print("Lista original con repetidos:", lista_con_repetidos) 
    lista_sin_repetidos = list(set(lista_con_repetidos)) # Crear una nueva lista sin elementos repetidos
    print("Lista sin elementos repetidos:", lista_sin_repetidos)
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal

"""5"""
def main(): # Función principal 
    estudiantes = [] # Lista para almacenar los nombres de los estudiantes
    for i in range(8):
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
        estudiantes.append(nombre) # Agregar el nombre a la lista
    print("Lista de estudiantes:", estudiantes) 
    accion = input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? ").strip().upper()
    if accion == "A":
        nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante) # Agregar el nuevo estudiante a la lista
        print(f"Estudiante '{nuevo_estudiante}' agregado.")
    elif accion == "E":
        estudiante_a_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
        if estudiante_a_eliminar in estudiantes:
            estudiantes.remove(estudiante_a_eliminar) # Eliminar el estudiante de la lista
            print(f"Estudiante '{estudiante_a_eliminar}' eliminado.")
        else:
            print(f"Estudiante '{estudiante_a_eliminar}' no encontrado en la lista.")
    else:
        print("Acción no válida. Por favor, ingrese 'A' para agregar o 'E' para eliminar.")
    print("Lista final actualizada de estudiantes:", estudiantes)
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal

"""6"""
def main(): # Función principal
    numeros = [] # Lista para almacenar los números
    for i in range(7):
        while True:
            try:
                numero = int(input(f"Ingrese el número {i + 1}: "))
                numeros.append(numero) # Agregar el número a la lista
                break
            except ValueError: #si ingresa letras en vez de números
                print("Entrada inválida. Por favor, ingrese un número válido.")
    print("Lista original:", numeros) 
    if len(numeros) > 0:
        ultimo_elemento = numeros.pop() # Eliminar el último elemento de la lista
        numeros.insert(0, ultimo_elemento) # Insertar el último elemento al inicio de la lista
    print("Lista después de rotar una posición a la derecha:", numeros)
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal

"""7""" 
def main(): # Función principal 
    temperaturas = [] # Lista para almacenar las temperaturas mínimas y máximas
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i in range(7):
        while True:
            try:
                temp_min = float(input(f"Ingrese la temperatura mínima del {dias_semana[i]}: "))
                temp_max = float(input(f"Ingrese la temperatura máxima del {dias_semana[i]}: "))
                if temp_min <= temp_max:
                    temperaturas.append([temp_min, temp_max]) # Agregar las temperaturas a la lista
                    break
                else:
                    print("La temperatura mínima no puede ser mayor que la máxima. Intente de nuevo.")
            except ValueError: #si ingresa letras en vez de números
                print("Entrada inválida. Por favor, ingrese un número válido.")
    print("Matriz de temperaturas (mínima, máxima):", temperaturas) 
    promedio_min = sum(temp[0] for temp in temperaturas) / len(temperaturas) # Calcular el promedio de las mínimas
    promedio_max = sum(temp[1] for temp in temperaturas) / len(temperaturas) # Calcular el promedio de las máximas
    print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}")
    print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")
    amplitudes = [temp[1] - temp[0] for temp in temperaturas] # Calcular las amplitudes térmicas diarias
    mayor_amplitud = max(amplitudes) # Encontrar la mayor amplitud térmica
    min_amplitud = min(amplitudes) # Encontrar la menor amplitud térmica
    dia_mayor_amplitud = dias_semana[amplitudes.index(mayor_amplitud)] # Encontrar el día correspondiente
    dia_menor_amplitud = dias_semana[amplitudes.index(min_amplitud)] # Encontrar el día correspondiente
    print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C, se registró el {dia_mayor_amplitud} y la menor amplitud térmica fue de {min_amplitud}°C, se registró el {dia_menor_amplitud}.")   
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal

"""8"""
def main(): # Función principal 
    estudiantes = [] # Lista para almacenar las notas de los estudiantes
    materias = ["Matemáticas", "Ciencias", "Historia"]
    for i in range(5):
        notas = [] # Lista para almacenar las notas de un estudiante
        print(f"Ingrese las notas del estudiante {i + 1}:")
        for materia in materias:
            while True:
                try:
                    nota = float(input(f"  Nota en {materia}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota) # Agregar la nota a la lista del estudiante
                        break
                    else:
                        print("Nota inválida. Por favor, ingrese una nota entre 0 y 10.")
                except ValueError: #si ingresa letras en vez de números
                    print("Entrada inválida. Por favor, ingrese un número válido.")
        estudiantes.append(notas) # Agregar las notas del estudiante a la lista principal
    print("Matriz de notas de los estudiantes:", estudiantes) 
    for i, notas in enumerate(estudiantes):
        promedio_estudiante = sum(notas) / len(notas) # Calcular el promedio del estudiante
        print(f"Promedio del estudiante {i + 1}: {promedio_estudiante:.2f}")
    for j in range(len(materias)):
        promedio_materia = sum(estudiantes[i][j] for i in range(len(estudiantes))) / len(estudiantes) # Calcular el promedio de la materia
        print(f"Promedio en {materias[j]}: {promedio_materia:.2f}")
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal

"""9"""
def mostrar_tablero(tablero): # Función para mostrar el tablero
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)
def main(): # Función principal
    tablero = [["-" for _ in range(3)] for _ in range(3)] # Inicializar el tablero con guiones
    jugadores = ["X", "O"]
    turno = 0
    for _ in range(9): # Máximo de 9 jugadas
        mostrar_tablero(tablero) # Mostrar el tablero actual
        jugador_actual = jugadores[turno % 2]
        while True:
            try:
                fila = int(input(f"Jugador {jugador_actual}, ingrese la fila (0, 1, 2): "))
                columna = int(input(f"Jugador {jugador_actual}, ingrese la columna (0, 1, 2): "))
                if 0 <= fila < 3 and 0 <= columna < 3:
                    if tablero[fila][columna] == "-":
                        tablero[fila][columna] = jugador_actual # Colocar la ficha en el tablero
                        break
                    else:
                        print("Casilla ya ocupada. Intente de nuevo.")
                else:
                    print("Posición inválida. Filas y columnas deben ser 0, 1 o 2.")
            except ValueError: #si ingresa letras en vez de números
                print("Entrada inválida. Por favor, ingrese números válidos para fila y columna.")
        turno += 1
    mostrar_tablero(tablero) # Mostrar el tablero final 
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal 
"""no supe como hacer que el juego termine cuando alguien gana o hay un empate"""

"""10"""
def main(): # Función principal 
    productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    ventas = [] # Matriz para almacenar las ventas de los productos
    for i in range(4):
        ventas_producto = [] # Lista para almacenar las ventas de un producto
        print(f"Ingrese las ventas del {productos[i]} durante la semana:")
        for j in range(7):
            while True:
                try:
                    venta = float(input(f"  Ventas del {dias_semana[j]}: "))
                    if venta >= 0:
                        ventas_producto.append(venta) # Agregar la venta a la lista del producto
                        break
                    else:
                        print("Venta inválida. Por favor, ingrese un valor no negativo.")
                except ValueError: #si ingresa letras en vez de números
                    print("Entrada inválida. Por favor, ingrese un número válido.")
        ventas.append(ventas_producto) # Agregar las ventas del producto a la matriz principal
    print("Matriz de ventas de los productos:", ventas) 
    total_por_producto = [sum(ventas[i]) for i in range(4)] # Calcular el total vendido por cada producto
    for i, total in enumerate(total_por_producto):
        print(f"Total vendido del {productos[i]}: {total:.2f}")
    total_por_dia = [sum(ventas[i][j] for i in range(4)) for j in range(7)] # Calcular el total vendido por cada día
    dia_mayores_ventas = dias_semana[total_por_dia.index(max(total_por_dia))] # Encontrar el día con mayores ventas totales
    print(f"Día con mayores ventas totales: {dia_mayores_ventas} con {max(total_por_dia):.2f} en ventas.")
    producto_mas_vendido = productos[total_por_producto.index(max(total_por_producto))] # Encontrar el producto más vendido en la semana
    print(f"Producto más vendido en la semana: {producto_mas_vendido} con {max(total_por_producto):.2f} en ventas.")
    dia_menores_ventas = dias_semana[total_por_dia.index(min(total_por_dia))] # Encontrar el día con menores ventas totales
    print(f"Día con menores ventas totales: {dia_menores_ventas} con {min(total_por_dia):.2f} en ventas.")
    producto_menos_vendido = productos[total_por_producto.index(min(total_por_producto))] # Encontrar el producto menos vendido en la semana
    print(f"Producto menos vendido en la semana: {producto_menos_vendido} con {min(total_por_producto):.2f} en ventas.")    
if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamada a la función principal 
