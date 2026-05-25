class Electrodomestico:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def encender(self):
        print(f"La {self.marca} {self.color} se encendio.")

class Lavadora(Electrodomestico):
    def __init__(self, marca, color, capacidad):
        super().__init__(marca, color)
        self.capacidad = capacidad
    
    def lavar(self):
        print(f"la lavadora {self.marca} esta lavando ropa con una capacidad de {self.capacidad}kg")

class Refrigerador(Electrodomestico):
    def __init__(self, marca, color, tiene_congelador):
        super().__init__(marca, color)
        self.tiene_congelador = tiene_congelador
    
    def mantener_frio(self):
        print(f"La nevera {self.marca} está manteniendo la comida fría.")

# ================== PRUEBAS ==================
lavadora1 = Lavadora("LG", "blanca", 15)
refrigerador1 = Refrigerador("Samsung", "plateada", True)

lavadora1.encender()
lavadora1.lavar()

refrigerador1.encender()
refrigerador1.mantener_frio()