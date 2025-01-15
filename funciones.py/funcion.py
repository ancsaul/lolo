class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}"

    def es_electrico(self):
        return True if self.marca == "Tesla" else False
    
# Inicializacion crear objetos a partir de clase
mi_auto = Auto("Volkswagen", "Jetta", "Morado")
print(mi_auto)
print(mi_auto.es_electrico())
mi_auto_2 = Auto("Tesla", "Model S", "Blanco")
print(mi_auto_2)
print(mi_auto_2.es_electrico())