class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        print(f"{self.nombre} está haciendo un sonido.")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)   
        self.raza = raza
    
    def ladrar(self):
        print(f"Guau guau soy un {self.raza} llamado {self.nombre}")


class Gato(Animal):
    def __init__(self, nombre, edad, color_pelaje):
        super().__init__(nombre, edad)
        self.color_pelaje = color_pelaje
    
    def ronronear(self):
        print(f"{self.nombre} el gato {self.color_pelaje} está ronroneando")


perro1 = Perro("Firulais", 5, "Pastor Alemán")
gato1 = Gato("Orion", 3, "gris")

perro1.hacer_sonido()
perro1.ladrar()

gato1.hacer_sonido()
gato1.ronronear()