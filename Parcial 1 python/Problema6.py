from collections import deque

# Definimos la estructura del producto
def crear_producto(id, nombre, cantidad, precio):
    return {
        'ID': id,
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio
    }

# Función para solicitar un número entero
def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")

# Función para solicitar un número decimal
def solicitar_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número decimal (use punto para decimales).")

# Función para agregar un producto al inventario
def agregar_producto(inventario):
    id = solicitar_entero("\nIngrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = solicitar_entero("Ingrese la cantidad: ")
    precio = solicitar_decimal("Ingrese el precio: ")

    # Verificar si ya existe el ID
    for producto in inventario:
        if producto['ID'] == id:
            print("\n¡Error! Ya existe un producto con ese ID.")
            return
    
    inventario.append(crear_producto(id, nombre, cantidad, precio))
    print("\nProducto agregado con éxito.")

# Función para modificar un producto en el inventario
def modificar_producto(inventario):
    id = solicitar_entero("\nIngrese el ID del producto a modificar: ")
    for producto in inventario:
        if producto['ID'] == id:
            nueva_cantidad = solicitar_entero("Ingrese la nueva cantidad: ")
            nuevo_precio = solicitar_decimal("Ingrese el nuevo precio: ")
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            print("\nProducto modificado con éxito.")
            return
    print("\nProducto no encontrado.")

# Función para eliminar un producto del inventario
def eliminar_producto(inventario):
    id = solicitar_entero("\nIngrese el ID del producto a eliminar: ")
    for producto in inventario:
        if producto['ID'] == id:
            inventario.remove(producto)
            print("\nProducto eliminado con éxito.")
            return
    print("\nProducto no encontrado.")

# Función para mostrar el inventario completo
def mostrar_inventario(inventario):
    print("\nInventario de productos:")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"ID: {producto['ID']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")

# Función para el menú interactivo
def menu():
    inventario = deque()
    while True:
        print("\n--- Inventario ---")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            modificar_producto(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            mostrar_inventario(inventario)
        elif opcion == '5':
            print("\n¡Saliendo del programa!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")

# Iniciar el programa
menu()