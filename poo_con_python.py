class personaje: 
    #atributos de la clase
    # nombre ='default'
    # fuerza = 0 
    # inteligencia = 0
    # vida = 0
   


    def __init__ (self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida
        self.inteligencia = inteligencia
        self.defensa = defensa


#¿que rayos significa self? referencia al mismo aobjeto
#¿que es init? constructor que inicializa el atributo del objeto
#¿por que tiene doble __ en el init? porque es un metodo magico (dunder)
#¿en que momento se ejecuta el momento init en poo python? cuando se crea un objeto

    def imprimir_atributos(self):
        print(self.nombre)
        print("-fuerza:", self.fuerza)
        print("-inteligencia:", self.inteligencia)
        print("-vida:", self.vida)
        print("-defensa:", self.defensa)


    def subir_nivel(self, fuerza, inteligencia):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, " ha muerto")
       # return self.vida <= 0

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa


    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, " ha ralizado", daño, "puntos de daño a", enemigo.nombre)
        print("vida de ", enemigo.nombre, "es", enemigo.vida)


#variable del constructor vacio de la clse
mi_personaje = personaje("dante", 100, 3, 100, 100)
mi_personaje.imprimir_atributos()
mi_personaje.subir_nivel(10,1)
mi_enemigo = personaje("vergil", 70, 30, 100, 70)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()


#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
# print ("--------------------")
# mi_personaje.imprimir_atributos()

# mi_personaje.nombre = "jojo"
# mi_personaje.fuerza = "30"
# mi_personaje.vida = "23"
# mi_personaje.inteligencia = "55"

#constructor de la clase

# print("el nombre del personaje es ", mi_personaje.nombre)
# print("la fuerza de mi personaje es ", mi_personaje.fuerza)
# print("la vida de mi personaje es ", mi_personaje.vida)
# print("la inteligencia de mi personaje es ", mi_personaje.inteligencia)