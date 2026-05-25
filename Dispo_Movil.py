class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def encender(self):
        print(f"el dispositivo {self.marca} {self.modelo} se está encendiendo.")

class Celular(Dispositivo):
    def __init__(self, marca, modelo, camara):
        super().__init__(marca, modelo)
        self.camara = camara
    
    def tomar_foto(self):
        print(f" Tomar una foto con la cámara de {self.camara}MP")

class Tablet(Dispositivo):
    def __init__(self, marca, modelo, pulgadas):
        super().__init__(marca, modelo)
        self.pulgadas = pulgadas
    
    def ver_pelicula(self):
        print(f" Ver una película en tablet de {self.pulgadas} pulgadas")


celular1 = Celular("iPhone", "15 Pro", 48)
tablet1 = Tablet("Samsung", "Galaxy Tab", 11)

celular1.encender()
celular1.tomar_foto()

tablet1.encender()
tablet1.ver_pelicula()