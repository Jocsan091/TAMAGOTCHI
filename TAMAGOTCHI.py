from datetime import date
import random



tipo = ["Ave", "Reptil", "Pez", "Anfibio", "Mamifero"]


class Mascotas:
    def __init__(self, nombre, fecha_de_nacimiento, tipo,): 
        self.nombre = nombre
        self.fecha_nacimiento = fecha_de_nacimiento
        self.tipo = tipo

        self.status_hungry = 50
        self.status_sleep = 50
        self.status_dirty = 50
        self.status_happyness = 50


    def mostrar_estado(self):
        print("nestado de la mascota:")
        print(f"Nombre: {self.nombre}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Tipo: {self.tipo}")
        print(f"Hambre: {self.status_hungry}")
        print(f"Sueño: {self.status_sleep}")
        print(f"Limpieza: {self.status_dirty}")
        print(f"Felicidad: {self.status_happyness}")

class ave(Mascotas):
    def __init__(self, nombre, fecha_de_nacimiento, tipo, status_hungry, status_sleep, status_dirty, status_happyness): 
        super().__init__(nombre, fecha_de_nacimiento, tipo, status_hungry, status_sleep, status_dirty, status_happyness)
        self.tipo = "ave"

print("Bienvenido a Tamagotchi")

nombre = input("Ingrese el nombre de su mascota: ")
fecha = str(date.today())   
tipo_aleatorio = random.choice(tipo)  


mascota = Mascotas(nombre, fecha, tipo_aleatorio)
print(f"Tipo asignado aleatoriamente: {tipo_aleatorio}")
mascota.mostrar_estado()





