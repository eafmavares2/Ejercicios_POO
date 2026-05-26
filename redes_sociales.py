class Usuario:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def login(self):
        print(f" {self.username} ha iniciado sesión.")

class Instagram(Usuario):
    def __init__(self, username, email, seguidores):
        super().__init__(username, email)
        self.seguidores = seguidores
    
    def subir_foto(self):
        print(f" {self.username} subió una foto (tiene {self.seguidores} seguidores)")

class Twitter(Usuario):
    def __init__(self, username, email, verificado):
        super().__init__(username, email)
        self.verificado = verificado
    
    def twittear(self):
        print(f" {self.username} publicó un tweet")

ig = Instagram("eryx.eai", "mavareseryx@gmail.com", 1000)
tw = Twitter("aquiles.castro", "aquiles@gmail.com", True)

ig.login()
ig.subir_foto()

tw.login()
tw.twittear()