class Mascotas:
    def __init__(self, nombre, fecha_de_nacimiento, tipo, status_hungry, status_sleep, status_dirty, status_happyness): 
        self.nombre = nombre
        self.fecha_nacimiento = fecha_de_nacimiento
        self.tipo = tipo
        self.status_hungry = status_hungry
        self.status_sleep = status_sleep
        self.status_dirty = status_dirty
        self.status_happyness = status_happyness 



class ave(Mascotas):
    def __init__(self, nombre, fecha_de_nacimiento, tipo, status_hungry, status_sleep, status_dirty, status_happyness): 
        super().__init__(nombre, fecha_de_nacimiento, tipo, status_hungry, status_sleep, status_dirty, status_happyness)
        self.tipo = "ave"
