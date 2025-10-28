"""1"""
with open("productos.txt", "w") as archivo: # Crear archivo inicial con productos
    archivo.write("Lapicera,129.5,30\n")
    archivo.write("Cuaderno,254.0,20\n")
    archivo.write("Mochila,3350.10,10\n")

"""2"""
with open("productos.txt", "r") as archivo: # Leer y mostrar productos
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",") # Procesar línea
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}") 

"""3"""
def agregar_producto():
    print("\n--- Agregar nuevo producto ---")
    nombre = input("Nombre del producto: ").strip() 
    precio = input("Precio: $ ").strip()
    cantidad = input("Cantidad: ").strip()
    with open("productos.txt", "a") as archivo: # Abrir archivo en modo agregar
        archivo.write(f"{nombre},{precio},{cantidad}\n") # Agregar nuevo producto
    print("Producto agregado exitosamente.")
agregar_producto()
    # Validar que el precio sea un número y la cantidad un entero
try:
        precio = float(precio)
        cantidad = int(cantidad)
except ValueError:
        print("Error: El precio debe ser un número y la cantidad un entero.")
        print ()


"""4"""
productos = [] # Lista para almacenar productos como diccionarios
print("\n--- Cargar productos en lista de diccionarios ---")
print ()    
with open("productos.txt", "r") as archivo: # Leer archivo y cargar en lista de diccionarios
    for linea in archivo: 
        nombre, precio, cantidad = linea.strip().split(",") 
        producto = { 
            "nombre": nombre,
            "precio": float(precio), # Convertir precio a float
            "cantidad": int(cantidad) # Convertir cantidad a int
        } # Crear diccionario del producto
        productos.append(producto) # Agregar diccionario a la lista
print("Lista de productos como diccionarios:")
print()
for producto in productos:
    print(producto) 

"""5"""
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
print()
if not nombre_buscar.isalpha(): # Verificar si el dato ingresado es texto
    print("Error: El nombre del producto debe ser texto.") 
else:
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower(): # Comparar nombres sin distinguir mayúsculas/minúsculas
            print(f"Producto encontrado: Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print ()
        print("Error: Producto no encontrado.")

"""6"""
with open("productos.txt", "w") as archivo: # Sobrescribir archivo con productos actualizados
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
print()    
print("Archivo productos.txt actualizado con los productos actuales.")
print() 
print("Contenido final del archivo productos.txt:")
print()
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
