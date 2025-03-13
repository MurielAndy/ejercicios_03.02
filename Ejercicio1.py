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


portatil = producto(1, "portatil", 666)
unidades = int(input("introduce unidades de portatil: "))
print("Total por", unidades, "unidades de", portatil.nombre, ":", round(portatil.calcular_total(unidades)),3)