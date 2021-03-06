from EVA2.producto import Producto
from EVA2.boleta import Boleta


#Antes de agregarlo deberíamos hacer las comprobaciones correspondientes

def validarNumero(pregunta):
    while True:
        try:
            numero = int(input(pregunta))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if type(numero) == float:
            print("Debes escribir un numero entero")
            continue

        if numero < 0:
            print("Debes escribir un número positivo.")
            continue

        else:
            break
    return numero


listaProductos = []


martillo = Producto.crearProducto(1, "martillo", 50, 2, 8000, 20, "makita", "herramientas", listaProductos)
taladro = Producto.crearProducto(2, "taladro", 50, 3, 30000, 15, "B&D", "herramientas", listaProductos)
cemento = Producto.crearProducto(3, "cemento", 40, 4, 40000, 15, "polpaico", "herramientas", listaProductos)
clavos = Producto.crearProducto(4, "clavos", 50, 5, 3000, 30, "genericos", "insumos", listaProductos)
tornillos = Producto.crearProducto(5, "tornillos", 100, 6, 2500, 50, "genericos", "insumos", listaProductos)
tuboPvc = Producto.crearProducto(6, "tubo pvc", 60, 7, 4000, 40, "makita", "herrasmientas", listaProductos)
pintura = Producto.crearProducto(7, "pintura", 50, 8, 6000, 30, "ceresita", "pinturas", listaProductos)
pastaMuro = Producto.crearProducto(8, "pasta muro", 60, 9, 10000, 35, "tajamar", "materiales", listaProductos)
desatornillador = Producto.crearProducto(9, "desatornillador", 30, 10, 4000, 35, "stanley", "herramientas", listaProductos)
diablo = Producto.crearProducto(10, "diablo", 20, 11, 8000, 20, "makita", "herramientas", listaProductos)
espatula = Producto.crearProducto(11, "espatula", 10, 1, 1000, 10, "makita", "herramientas", listaProductos)


listaBoleta = []

idBoleta = 1
productoEncontrado = False

Producto.traerProductos(listaProductos)

while True:
    productoEncontrado = False
    print("\nMenú de Opciones")
    print("1. Mantenedor de Productos/Precios")
    print("2. Generar boleta (venta)")
    print("3. Buscar una boleta emitida")
    print("4. Salir/Finalizar")

    opcion = validarNumero("Ingrese una opción (1-4): ")

    while opcion < 1 or opcion > 4:
        opcion = validarNumero("Ingrese una opción (1-4): ")

    if opcion==1:
        print("\nMantenedor de productos/precios")
        print("1. Agregar producto")
        print("2. Mostrar producto por ID")
        print("3. Mostrar listado completo de productos")
        print("4. Actualizar un producto")
        print("5. Eliminar un producto")
        opcionProducto = validarNumero("Ingrese una opción (1-5): ")
        while opcionProducto > 5 or opcionProducto < 1:
            opcionProducto = validarNumero("Ingrese una opción (1-5): ")

        if opcionProducto == 1:
            print("\nAgregando producto...")
            nuevoProductoId = len(listaProductos)+1
            print("\nID nuevo producto: ", nuevoProductoId)
            nombre = input("\nIngrese nombre del producto: ")
            nombre = nombre.lower()
            preciolista = validarNumero("Ingrese precio: ")
            while preciolista < 1:
                preciolista = validarNumero("Ingrese precio: ")
            ganancia = validarNumero("Ingrese porcentaje de ganancia %: ")
            while ganancia < 1:
                ganancia = validarNumero("Ingrese porcentaje de ganancia %: ")
            stock = validarNumero("Ingrese stock: ")
            while stock < 1:
                stock = int(input("Ingrese stock: "))
            proveedor = input("Ingrese proveedor: ")
            categoria = input("Ingrese categoría: ")

            nuevoProducto = Producto.crearProducto(nuevoProductoId, nombre, stock, nuevoProductoId, preciolista, ganancia, proveedor, categoria, listaProductos)
            print("\nNuevo producto agregado: ", nuevoProducto)
        elif opcionProducto == 2:

            idProducto = validarNumero("Ingrese el id del producto a buscar: ")
            while idProducto > len(listaProductos) or idProducto < 1:
                print("No existe ningun producto asociado al id {}".format(idProducto))
                idProducto = validarNumero("Ingrese un id entre {} y {} : ".format(1, len(listaProductos)))
            Producto.traerProducto(idProducto, listaProductos)

        elif opcionProducto == 3:
            Producto.traerProductos(listaProductos)

        elif opcionProducto == 4:

            Producto.traerProductos(listaProductos)
            print("\nActualizando producto...")
            print("1. Buscar por ID")
            print("2. Buscar por Nombre")
            buscar = validarNumero("Ingrese opción (1-2): ")
            while buscar > 2 or buscar < 1:
                buscar = validarNumero("Ingrese opción (1-2): ")

            if buscar == 1:
                idBuscar = validarNumero("Ingrese ID:")
                while idBuscar > len(listaProductos):
                    idBuscar = validarNumero("Ingrese un ID entre {} y {}:".format(1, len(listaProductos)))
                for articulo in listaProductos:
                    if articulo.idproducto == idBuscar:
                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                        nuevoStock = validarNumero("Ingrese el nuevo stock del producto: ")
                        nuevoProveedor = input("Ingrese el nuevo proveedor: ")
                        nuevaCategoria = input("Ingrese la nueva categoría: ")
                        nuevoPrecio = validarNumero("Ingrese nuevo precio: ")
                        nuevaGanancia = validarNumero("Ingrese un nuevo porcentaje de ganancia en número: ")
                        Producto.actualizarProducto(idBuscar,nuevoNombre, nuevoStock, nuevoPrecio, nuevaGanancia, nuevoProveedor, nuevaCategoria, listaProductos)


            if buscar == 2:
                nombreBuscar = input("Ingrese nombre: ")
                nombreBuscar = nombreBuscar.lower()
                while type(nombreBuscar) != str:
                    nombreBuscar = input("Ingrese nombre: ")
                for articulo in listaProductos:
                    if articulo.nombre == nombreBuscar:
                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                        nuevoStock = validarNumero("Ingrese el nuevo stock del producto: ")
                        nuevoProveedor = input("Ingrese el nuevo proveedor: ")
                        nuevaCategoria = input("Ingrese la nueva categoría: ")
                        nuevoPrecio = validarNumero("Ingrese nuevo precio: ")
                        nuevaGanancia = validarNumero("Ingrese un nuevo porcentaje de ganancia en número: ")
                        Producto.actualizarProductoPorNombre(nombreBuscar, nuevoNombre, nuevoStock, nuevoPrecio, nuevaGanancia,
                                                    nuevoProveedor, nuevaCategoria, listaProductos)

        elif opcionProducto == 5:
            idEliminar = validarNumero("Ingrese el id del producto a eliminar: ")
            Producto.eliminarProducto(idEliminar, listaProductos)




    elif opcion==2:
        numeroBoleta = 1
        carritoCompra = []

        print("\nGenerando boleta N°{}".format(numeroBoleta))
        print("1. Seleccionar producto por ID")
        print("2. Seleccionar producto por Nombre")
        buscar = validarNumero("Ingrese opción (1-2): ")
        while buscar > 2 or buscar < 1:
            buscar = validarNumero("Ingrese opción (1-2): ")



        Producto.traerProductos(listaProductos)

        respuesta = True

        while respuesta == True:

            if buscar == 1:
                productoEncontrado = False
                Producto.traerProductos(listaProductos)
                idBuscar = validarNumero("Ingrese ID:")

                while idBuscar > len(listaProductos) or idBuscar < 1:
                    idBuscar = validarNumero("Ingrese ID válido entre {} y {}:".format(1, len(listaProductos)))

                for articulo in listaProductos:
                    if articulo.idproducto == idBuscar:
                        productoEncontrado = True
                        if articulo.stock < 1 or articulo.stock == 0:
                            print("No hay stock de {}".format(articulo.nombre))
                            continue

                        print("Producto seleccionado", articulo)
                        cantidad = validarNumero("Ingrese cantidad: ")
                        while cantidad < 1:
                            cantidad = validarNumero("Ingrese cantidad mayor a 0: ")
                        cantidadStock = articulo.validarStock(cantidad)
                        if cantidadStock == True or cantidadStock == cantidad:
                            articulo.restarStock(cantidad)
                            boletaGenerada = Boleta(idBoleta, numeroBoleta, articulo, cantidad)
                            numeroBoleta += 1
                            carritoCompra.append(boletaGenerada)
                            print(boletaGenerada.mostrarBoleta())
                        elif cantidadStock < cantidad:
                            res = input(
                                "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(articulo.nombre,
                                                                                                      cantidadStock))
                            res = res.lower()
                            while res != "si" and res != "no":
                                res = input(
                                    "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(
                                        articulo.nombre,
                                        cantidadStock))
                                res = res.lower()
                            if res == "si":
                                articulo.restarStock(cantidadStock)
                                boletaGenerada = Boleta(idBoleta, numeroBoleta, articulo, cantidadStock)
                                numeroBoleta += 1
                                carritoCompra.append(boletaGenerada)
                                print(boletaGenerada.mostrarBoleta())
                            else:
                                break

                if productoEncontrado == False:
                    print("No se ha encontrado el producto con ID '{}'".format(idBuscar))

            if buscar == 2:
                productoEncontrado = False
                Producto.traerProductos(listaProductos)
                nombreBuscar = input("Ingrese nombre: ")
                nombreBuscar = nombreBuscar.lower()
                for articulo in listaProductos:
                    if articulo.nombre == nombreBuscar:
                        productoEncontrado = True
                        if articulo.stock < 1 or articulo.stock == 0:
                            print("No hay stock de {}".format(articulo.nombre))
                            continue

                        print("Producto seleccionado", articulo)
                        cantidad = validarNumero("Ingrese cantidad: ")

                        while cantidad < 1:
                            cantidad = validarNumero("Ingrese cantidad mayor a 0: ")
                        cantidadStock = articulo.validarStock(cantidad)
                        if cantidadStock == True:
                            articulo.restarStock(cantidad)
                            boletaGenerada = Boleta(idBoleta, numeroBoleta, articulo, cantidad)
                            numeroBoleta += 1
                            carritoCompra.append(boletaGenerada)
                            print(boletaGenerada.mostrarBoleta())
                        elif type(cantidadStock) == int:
                            res = input(
                                "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(articulo.nombre,
                                                                                                      cantidadStock))
                            res = res.lower()
                            while res != "si" and res != "no":
                                res = input(
                                    "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(
                                        articulo.nombre,
                                        cantidadStock))
                                res = res.lower()
                            if res == "si":
                                articulo.restarStock(cantidadStock)
                                boletaGenerada = Boleta(idBoleta, numeroBoleta, articulo, cantidadStock)
                                numeroBoleta += 1
                                carritoCompra.append(boletaGenerada)
                                print(boletaGenerada.mostrarBoleta())
                            else:
                                break

                if productoEncontrado == False:
                    print("No se ha encontrado el producto  '{}'".format(nombreBuscar))


            respuesta = input("¿Desea comprar un nuevo producto? SI/NO")
            respuesta.lower()

            while respuesta != "si" and respuesta != "no":
                respuesta = input("¿Desea comprar un nuevo producto? SI/NO")
                respuesta.lower()
            if respuesta == "si":
                respuesta = True
            elif respuesta == "no":
                for producto in carritoCompra:
                    print(producto.mostrarCarrito())


                respuestaCarrito = input("¿Desea eliminar algun producto del carrito? SI/NO")
                respuestaCarrito.lower()
                while respuestaCarrito != "si" and respuestaCarrito != "no":
                    respuesta = input("¿Desea eliminar algun producto del carrito? SI/NO")
                    respuesta.lower()
                while respuestaCarrito == "si":
                    idEliminar = validarNumero("Ingrese el id del producto a eliminar: ")
                    while idEliminar < 1 or idEliminar > len(carritoCompra):
                        idEliminar = validarNumero("Ingrese un id entre {} y {}: ".format(1, len(carritoCompra)))
                    carritoCompra.pop(idEliminar - 1)

                    if len(carritoCompra) >= 1:
                        for producto in carritoCompra:
                            print(producto.mostrarCarrito())

                        respuestaCarrito = input("¿Desea eliminar otro producto del carrito? SI/NO")
                        respuestaCarrito.lower()
                        while respuestaCarrito != "si" and respuestaCarrito != "no":
                            respuestaCarrito = input("¿Desea eliminar otro producto del carrito? SI/NO")
                            respuesta.lower()
                    else:
                        print("El carrito esta vacío, será devuelto al menu...")
                        break

                if respuestaCarrito == "no":
                    listaBoleta.append(carritoCompra)
                    for boleta in listaBoleta:
                        if boleta[0].idboleta == idBoleta:
                            tabla = """ 
                            \tEMISION DE BOLETA
                             _________________________________________________
                            | Python Store                                    |
                            | Ferretería                                      |
                            |         Boleta de ventas y servicios            |
                            |  Boleta Nº{:3d}                                   |
                            |_________________________________________________|
                            | Cantidad | Descripción    |  Precio  | Subtotal |
                            |__________|________________|__________|__________|
                            """.format(idBoleta)

                            total = 0

                            for producto in boleta:
                                tabla += "| {:3d}      |{:16s}|{:7,.0f}   |{:7,.0f}   |".format(producto.cantidad, producto.producto.nombre, producto.precio, producto.subtotal).replace(',','.')
                                total += producto.subtotal
                                tabla += "\n"
                                tabla += "\t\t\t\t\t\t\t"

                            tabla += "|__________|________________|__________|__________|"
                            tabla += """\n
                            \t\t\t\t\t\t\t\t Total Neto: {:,.0f}
                            \t\t\t\t\t\t\t\t IVA       : {:,.0f}
                            \t\t\t\t\t\t\t\t A Pagar   : {:,.0f}
                            """.format(total, total * 0.19, total + total * 0.19).replace(',','.')

                            print(tabla)

                    idBoleta += 1
                    respuesta = False


    elif opcion == 3:
        if len(listaBoleta) < 1:
            print("No existen boletas emitidas...")
        else:
            idBoleta = validarNumero("Ingrese la boleta a buscar: ")
            while idBoleta < 1 or idBoleta > len(listaBoleta):
                idBoleta = validarNumero("Existen {} Boletas, ingrese un número válido ".format(len(listaBoleta)))
            print("Buscando boleta {}...".format(idBuscar))
            for boleta in listaBoleta:
                print("Boleta N°{}".format(boleta[0].idboleta))
                for producto in boleta:
                    if producto.idboleta == idBoleta:
                        tabla = """ 
                        \tEMISION DE BOLETA EMITIDA
                         _________________________________________________
                        | Python Store                                    |
                        | Ferretería                                      |
                        |         Boleta de ventas y servicios            |
                        |  Boleta Nº{:3d}                                   |
                        |_________________________________________________|
                        | Cantidad | Descripción    |  Precio  | Subtotal |
                        |__________|________________|__________|__________|
                        """.format(idBoleta)

                        total = 0

                        for producto in boleta:
                            tabla += "| {:3d}      |{:16s}|{:7,.0f}   |{:7,.0f}   |".format(producto.cantidad,
                                                                                            producto.producto.nombre,
                                                                                            producto.precio,
                                                                                            producto.subtotal).replace(
                                ',', '.')
                            total += producto.subtotal
                            tabla += "\n"
                            tabla += "\t\t\t\t\t\t"

                        tabla += "|__________|________________|__________|__________|"
                        tabla += """\n
                        \t\t\t\t\t\t\t\t Total Neto: {:,.0f}
                        \t\t\t\t\t\t\t\t IVA       : {:,.0f}
                        \t\t\t\t\t\t\t\t A Pagar   : {:,.0f}
                        """.format(total, total * 0.19, total + total * 0.19).replace(',', '.')

                        print(tabla)
                print("\n")
    elif opcion == 4:
        print("Cerrando Programa...")
        break

    else:
        print("\nProceso finalizado....")
        break




