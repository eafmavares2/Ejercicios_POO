class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}")

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
    
    def enseñar(self):
        print(f"El profesor {self.nombre} está enseñando {self.materia}")


estudiante1 = Estudiante("Eryx", 18, "Desarrollo de software")
profesor1 = Profesor("David", 45, "Matemáticas")

estudiante1.presentarse()
estudiante1.estudiar()

profesor1.presentarse()
profesor1.enseñar()