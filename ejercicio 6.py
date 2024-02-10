#ejercicio 6
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print("Nombre:", producto.nombre)
            print("Precio:", producto.precio)
            print("Año:", producto.año)
            print()

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print("Nombre:", producto.nombre)
                print("Precio:", producto.precio)
                print("Año:", producto.año)
                print()

def main():
    catalogo = Catalogo()

    # Agregar algunos productos al catálogo
    producto1 = Producto("Llantas", 100, 2022)
    producto2 = Producto("Batería", 150, 2021)
    producto3 = Producto("Aceite", 30, 2022)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar todos los productos
    catalogo.mostrar_productos()

    # Filtrar productos por año
    catalogo.filtrar_por_año(2022)

if __name__ == "__main__":
    main()
