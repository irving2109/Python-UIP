PLAN - SISTEMA DE GESTION DE INVENTARIO DE UNA TIENDA DE FRUTAS Y VERDURAS.

1. CLASES PRINCIPALES Y ESTRUCTURAS DE DATOS
1.1 Clase Producto
Representa los productos disponibles en la tienda (legumbres, frutas, etc.).




Lo mio es atributos (hacer abajo)


Atributos:
id_producto: ID único del producto.
nombre: Nombre del producto.                            
descripcion: Descripción del producto.
categoria: Categoría del producto (ej. Verduras, Frutas, etc.).
precio: Precio de venta por unidad.
stock: Cantidad disponible en inventario.
fecha_expiracion: Fecha de expiración (si aplica).
temporalidad: Indica si el producto es de temporada.
rebaja: Descuento aplicable al producto si está cerca de su fecha de expiración.



Lo mio  es funciones (hacer abajo) 


Funciones:
registrar_producto(): Registra un nuevo producto.
actualizar_producto(): Actualiza la información de un producto.
eliminar_producto(): Elimina un producto del inventario.
consultar_producto(): Consulta información de un producto por su ID o nombre.
aplicar_rebaja(): Aplica una rebaja a productos cercanos a su fecha de expiración.

1.2 Clase Proveedor
Representa a los proveedores que suministran los productos.

Atributos:
id_proveedor: ID único del proveedor.
nombre: Nombre del proveedor.
contacto: Información de contacto (teléfono, correo).
direccion: Dirección del proveedor.

Funciones:
registrar_proveedor(): Registra un nuevo proveedor.
actualizar_proveedor(): Modifica la información de un proveedor.
eliminar_proveedor(): Elimina un proveedor del sistema.
consultar_proveedor(): Consulta información de un proveedor por su ID o nombre.

1.3 Clase Cliente
Representa a los clientes que realizan compras.

Atributos:
id_cliente: ID único del cliente.
nombre: Nombre del cliente.
contacto: Información de contacto (teléfono, correo).
direccion: Dirección del cliente.
tipo_cliente: Tipo de cliente (ej. minorista, mayorista).
credito: Crédito disponible (opcional).

Funciones:
registrar_cliente(): Registra un nuevo cliente.
actualizar_cliente(): Actualiza la información de un cliente.
eliminar_cliente(): Elimina un cliente del sistema.
consultar_cliente(): Consulta información de un cliente por su ID o nombre.

1.4 Clase Transacción
Representa las ventas realizadas a los clientes.

Atributos:
id_transaccion: ID único de la transacción.
id_cliente: ID del cliente que realiza la compra.
productos: Lista de productos comprados.
total: Total de la transacción.
fecha: Fecha de la transacción.
tipo_pago: Método de pago (efectivo, tarjeta, crédito).
estado: Estado de la transacción (pendiente, completada, cancelada).

Funciones:
registrar_transaccion(): Registra una venta realizada.
actualizar_transaccion(): Actualiza la información de una transacción.
eliminar_transaccion(): Elimina una transacción.
consultar_transacciones(): Consulta las transacciones por cliente o fecha.

1.5 Clase EstadoMovimiento
Gestión y consulta de movimientos (ventas, compras) por fechas o tipo de transacción.

Atributos:
id_estado: ID único del movimiento.
id_transaccion: ID de la transacción relacionada.
fecha: Fecha en que se realizó el movimiento.
tipo: Tipo de movimiento (compra/venta).

Funciones:
consultar_movimiento_por_fecha(): Consulta movimientos (ventas o compras) por fecha.
consultar_movimiento_por_tipo(): Consulta movimientos por tipo (compra o venta).

1.6 Clase RotaciónInventario
Clase adicional para manejar la rotación del inventario.

Atributos:
productos_temporada: Lista de productos de temporada.
productos_rebajados: Lista de productos con rebaja por fecha de expiración próxima.
Funciones:
verificar_temporada(): Verifica si un producto está dentro de la temporada correspondiente.
verificar_rebaja(): Verifica si un producto tiene una rebaja aplicada por proximidad a la fecha de expiración.

2. ESTRUCTURA DE LA BASE DE DATOS
2.1 Tabla productos:
id_producto: INTEGER PRIMARY KEY AUTOINCREMENT.
nombre: TEXT.
descripcion: TEXT.
categoria: TEXT.
precio: DECIMAL.
stock: INTEGER.
fecha_expiracion: DATE.
temporalidad: BOOLEAN.
rebaja: DECIMAL.

2.2 Tabla proveedores:
id_proveedor: INTEGER PRIMARY KEY AUTOINCREMENT.
nombre: TEXT.
contacto: TEXT.
direccion: TEXT.

2.3 Tabla clientes:
id_cliente: INTEGER PRIMARY KEY AUTOINCREMENT.
nombre: TEXT.
contacto: TEXT.
direccion: TEXT.
tipo_cliente: TEXT.
credito: DECIMAL (default 0).

2.4 Tabla transacciones:
id_transaccion: INTEGER PRIMARY KEY AUTOINCREMENT.
id_cliente: INTEGER (FK -> clientes).

productos: TEXT (Lista de productos comprados en formato JSON).
total: DECIMAL.
fecha: DATE.
tipo_pago: TEXT.
estado: TEXT.

2.5 Tabla estado_movimiento:
id_estado: INTEGER PRIMARY KEY AUTOINCREMENT.
id_transaccion: INTEGER (FK -> transacciones).
fecha: DATE.
tipo: TEXT (compra/venta).

2.6 Tabla rotación_inventario:
id_producto: INTEGER (FK -> productos).
fecha_inicio: DATE.
fecha_fin: DATE.
tipo: TEXT (temporalidad o rebaja).

3. FLUJO DE OPERACIONES EN EL SISTEMA
3.1 Gestión de Inventario:
Producto: Los productos se gestionan mediante la clase Producto, y se actualizan según el stock disponible, la expiración, y las rebajas aplicadas. Los productos de temporada serán manejados separadamente para garantizar que solo se vendan cuando estén disponibles.

Rotación de Inventario: La clase RotaciónInventario se encargará de gestionar las fechas de entrada y salida de productos, 
clasificando los productos según su temporalidad y aplicando rebajas a aquellos que están por expirar.

3.2 Registro de Proveedores:
Los proveedores se gestionan mediante la clase Proveedor, lo que facilita el registro y actualización de datos sobre quién suministra los productos. Este módulo garantiza que siempre haya un registro de proveedores actualizado para obtener productos.

3.3 Gestión de Clientes:
Los clientes se gestionan mediante la clase Cliente, con soporte para su tipo (minorista, mayorista) y un sistema de crédito. 
Además, las transacciones se pueden registrar y consultar para hacer un seguimiento de los pagos.

3.4 Registro de Transacciones:
Las ventas se registran mediante la clase Transacción. Cada transacción está asociada a un cliente y se almacenan los productos vendidos, 
el total de la venta, la fecha y los detalles de pago. Las transacciones pueden ser consultadas por fecha o por cliente, lo que permite 
tener un control eficiente de ventas.

3.5 Consulta de Movimientos:
A través de la clase EstadoMovimiento, se pueden consultar los movimientos de inventario (ventas y compras) 
para obtener información sobre la rotación de los productos en el tiempo. Esta clase ayuda a mantener un seguimiento de las operaciones de compra 
y venta realizadas.

4. CASOS ESPECIALES DE ROTACIÓN DE INVENTARIO
4.1 Productos por Temporada:
Se debe implementar un sistema que marque ciertos productos como de temporada. 
Esto asegurará que dichos productos solo estén disponibles para su venta durante ciertas épocas del año.

4.2 Rebajas por Productos a Punto de Expirar:
Los productos cercanos a su fecha de expiración tendrán descuentos automáticos, 
registrados a través del atributo rebaja de la clase Producto. Estos productos deberán ser visualizados 
en una categoría especial de "Rebajas" para atraer a los clientes.

4.3 Gestión de Inventarios por Fecha y Tipo:
La base de datos y las clases estarán estructuradas para que se pueda consultar inventarios por fecha y tipo de transacción. 
Los movimientos de inventario se registrarán en la tabla estado_movimiento para consultas rápidas.
