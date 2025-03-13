class producto():
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        
    
    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precio(self, precio):
        self.precio = precio
    
    def get_codigo(self):
        return self.codigo
    
    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio

    def calcular_total(self, unidades):
        total = self.precio * unidades
        return total

class pedido():
    def __init__(self, ListaProductos, ListaCantidades):
        self.ListaProductos = ListaProductos
        self.ListaCantidades = ListaCantidades

    def total_pedido(self):
        total = 0
        for i in range(len(self.ListaProductos)):
            total += self.ListaProductos[i].calcular_total(self.ListaCantidades[i])
        return total
    
    def mostrar_productos(self):
        for i in range(len(self.ListaProductos)):
            print(self.ListaCantidades[i], "x", self.ListaProductos[i].nombre, self.ListaProductos[i].precio, "Euros")       


portatil = producto(1, "portatil", 666)
raton = producto(2, "Ratón", 20)

unidades_portatil = int(input("introduce unidades de portatil: "))
unidades_raton = int(input("Introduce unidades de ratón: "))

pedido1 = pedido([portatil, raton], [unidades_portatil, unidades_raton])

print("\nProductos en el pedido:")
pedido1.mostrar_productos()
print("\nTotal del pedido:", round(pedido1.total_pedido(), 3))