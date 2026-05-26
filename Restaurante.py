class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def info(self):
        print(f"{self.nombre} : ${self.precio}")

class Comida(Producto):
    def __init__(self, nombre, precio, calorias):
        super().__init__(nombre, precio)
        self.calorias = calorias
    
    def cocinar(self):
        print(f"Cocinando una {self.nombre}")

class Bebida(Producto):
    def __init__(self, nombre, precio, es_alcoholica):
        super().__init__(nombre, precio)
        self.es_alcoholica = es_alcoholica
    
    def servir(self):
        print(f"Sirviendo la {self.nombre}")

hamburguesa = Comida("Hamburguesa", 3.5, 650)
coca = Bebida("Colita ", 1.5, False)

hamburguesa.info()
hamburguesa.cocinar()

coca.info()
coca.servir()