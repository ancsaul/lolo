class personaje: 
    #atributos de la clase
    nombre ='default'
    fuerza = 0 
    inteligencia = 0
    vida = 0
    sexo = 0
    #indicar que no se haga nada 
    pass
#variable del constructor vacio de la clse
mi_personaje = personaje()
mi_personaje.nombre = "chemaputo"
mi_personaje.fuerza = "30"
mi_personaje.vida = "23"
mi_personaje.inteligencia = "55"


print("el nombre del personaje es ", mi_personaje.nombre)
print("la fuerza de mi personaje es ", mi_personaje.fuerza)
print("la vida de mi personaje es ", mi_personaje.vida)
print("la inteligencia de mi personaje es ", mi_personaje.inteligencia)
