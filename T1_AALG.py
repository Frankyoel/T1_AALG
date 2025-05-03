import random


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partGanados = 0
        self.partPerdidos = 0
        self.setGanados = 0

equipo1 = Equipo("Kastoy")
equipo2 = Equipo("Keleep")


#funcion para resgistar los sets
def RegistraSet(equipo_1o2):
    if equipo_1o2 == 1:
        equipo1.setGanados += 1
        if equipo1.setGanados == 3:
            equipo1.partGanados += 1
            equipo2.partPerdidos += 1
            # Resetear sets para nuevo partido
            equipo1.setGanados = 0
            equipo2.setGanados = 0
    elif equipo_1o2 == 2:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partGanados += 1
            equipo1.partPerdidos += 1
            # Resetear sets para nuevo partido
            equipo1.setGanados = 0
            equipo2.setGanados = 0

#funcion para puntos
def Puntos():
    return random.randint(10,28)

#funcion para puntos extras
def PuntosExtras():
    return random.randint(0, 6)

#funcion de JugarPartido
def jugarPartido():
    #Simular un partido hasta que un equipo logre 3 sets
    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        puntos1 = Puntos()
        puntos2 = Puntos()
        
        # Verificar si alguno alcanzó 25 puntos
        while True:
            if puntos1 >= 25 and puntos1 > puntos2:
                print(f"{equipo1.nombre} ganó el set con {puntos1} puntos vs {puntos2}")
                RegistraSet(1)
                break
            elif puntos2 >= 25 and puntos2 > puntos1:
                print(f"{equipo2.nombre} ganó el set con {puntos2} puntos vs {puntos1}")
                RegistraSet(2)
                break
            else:
                # Ninguno alcanzó 25, sumar puntos extras
                puntos1 += PuntosExtras()
                puntos2 += PuntosExtras()


# Función ResultadoTorneo
def ResultTorneo():
    print("\n RESULTADOS DEL TORNEO ")
    print(f"{equipo1.nombre}: P Ganados = {equipo1.partGanados} \n P Perdidos = {equipo1.partPerdidos}") 
    print(f"{equipo2.nombre}: P Ganados = {equipo2.partGanados} \n P Perdidos = {equipo2.partPerdidos}")

def main():

    #Partido por jugar
    num_part = int(input("Ingrese el número de partidos a jugar: "))
    for i in range(num_part):
        print(f"\nPartido {i+1} de {num_part}")
        jugarPartido()
    
    ResultTorneo()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
