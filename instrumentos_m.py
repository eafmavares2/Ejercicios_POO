class Instrumento:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def tocar(self):
        print(f" Se está tocando un instrumento marca {self.marca}.")

class Guitarra(Instrumento):
    def __init__(self, marca, color, tipo):
        super().__init__(marca, color)
        self.tipo = tipo  # eléctrica, acústica
    
    def rasguear(self):
        print(f" Rasgueando la guitarra {self.tipo} {self.marca}")

class Piano(Instrumento):
    def __init__(self, marca, color, teclas):
        super().__init__(marca, color)
        self.teclas = teclas
    
    def tocar_teclas(self):
        print(f" tocando un piano de {self.teclas} teclas")

guitarra1 = Guitarra("Fender", "negra", "eléctrica")
piano1 = Piano("Yamaha", "madera", 100000)

guitarra1.tocar()
guitarra1.rasguear()

piano1.tocar()
piano1.tocar_teclas()