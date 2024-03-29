class Vehiculo:
    def __init__(self, color, rueda):
        self.color = color
        self.rueda = rueda

    def __str__(self):
        return f'Vehiculo [Color: {self.color}, Ruedas: {self.rueda}]'


class Coche(Vehiculo):
    def __init__(self, color, rueda, velocidad):
        super().__init__(color, rueda)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.velocidad}'


class Bicicleta(Vehiculo):
    def __init__(self, color, rueda, tipo):
        super().__init__(color, rueda)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} Tipo: {self.tipo}'
