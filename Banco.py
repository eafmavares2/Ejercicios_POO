class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def mostrar_saldo(self):
        print(f"El saldo de {self.titular}: ${self.saldo}")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self.interes = interes
    
    def calcular_interes(self):
        print(f"Su interés anual es: {self.interes}%")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, sobregiro):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro
    
    def mostrar_info(self):
        print(f"La cuenta corriente de {self.titular} tiene un sobregiro de ${self.sobregiro}")


ahorro = CuentaAhorro("Eryx Mavares", 0.01, 0)
corriente = CuentaCorriente("Pepe el grillo", 10, 5)

ahorro.mostrar_saldo()
ahorro.calcular_interes()

corriente.mostrar_saldo()
corriente.mostrar_info()