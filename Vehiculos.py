class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def mover(self):
        print(f"El {self.marca} {self.color} está arrancando.")

class Carro(Vehiculo):
    def __init__(self, marca, color, puertas):
        super().__init__(marca, color)
        self.puertas = puertas
    
    def tocar_bocina(self):
        print(f"pippppp tengo un {self.marca} con {self.puertas} puertas.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, color, cilindrada):
        super().__init__(marca, color)
        self.cilindrada = cilindrada
    
    def hacer_caballito(self):
        print(f"La {self.marca} de {self.cilindrada}cc está haciendo caballito!")

carro = Carro("Toyota", "rojo", 4)
moto = Motocicleta("Yamaha", "negra", 250)
carro.mover()
carro.tocar_bocina()
moto.hacer_caballito()