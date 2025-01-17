class Casa:
    def __init__(self, year, place, mtrs, sell, remodel):
        self.year = year
        self.place = place
        self.mtrs = mtrs
        self.sell = sell
        self.remodel = remodel

    def __str__(self):
        return f"Año: {self.year}\nLugar: {self.place}\nMetros de construcción: {self.mtrs}\nVendida: {self.sell}\nRemodelada: {self.remodel}"

    def remodelada(self, status): 
        self.remodel = status

    def vendida(self, status):
        self.sell = status

casa_1 = Casa("1999", "Fco de montejo", "3000 mtr^2", False, False)
casa_1.vendida(True)
casa_1.remodelada(False)
print(casa_1)