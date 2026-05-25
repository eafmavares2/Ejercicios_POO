class Figura:
    def __init__(self, color):
        self.color = color
    
    def describir(self):
        print(f"Esta es una figura de color {self.color}.")

class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
    
    def area(self):
        print(f"Área del rectángulo: {self.base * self.altura} cm²")

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        print(f"Área del círculo: {3.14 * self.radio**2:.2f} cm²")

rect = Rectangulo("azul", 10, 5)
circ = Circulo("rojo", 7)

rect.describir()
rect.area()

circ.describir()
circ.area()