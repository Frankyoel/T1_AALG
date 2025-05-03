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
            return True
    elif equipo_1o2 == 2:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partGanados += 1
            equipo1.partPerdidos += 1
            # Resetear sets para nuevo partido
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            return True

#funcion para puntos
def Puntos():
    return random.randint(10,28)

#funcion para puntos extras
def PuntosExtras():
    return random.randint(0, 6)

#funcion de JugarPartido
def jugarPartido():
    print(f"\nNuevo partido: {equipo1.nombre} vs {equipo2.nombre}")

    partido_terminado = False

    while not partido_terminado:
        puntos1 = Puntos()
        puntos2 = Puntos()
        extras1 = 0
        extras2 = 0

        while True:
            if puntos1 >= 25 and puntos1 > puntos2:
                print(f"{equipo1.nombre} ganó el set con {puntos1} puntos vs {puntos2}")
                partido_terminado = RegistraSet(1)
                break
            elif puntos2 >= 25 and puntos2 > puntos1:
                print(f"{equipo2.nombre} ganó el set con {puntos2} puntos vs {puntos1}")
                partido_terminado = RegistraSet(2)
                break
            else:
                extras1 = PuntosExtras()
                extras2 = PuntosExtras()
                puntos1 += extras1
                puntos2 += extras2


# Función ResultadoTorneo
def ResultTorneo():
    print("\n RESULTADOS DEL TORNEO ")
    print(f"{equipo1.nombre}: P Ganados = {equipo1.partGanados} \n P Perdidos = {equipo1.partPerdidos}") 
    print(f"{equipo2.nombre}: P Ganados = {equipo2.partGanados} \n P Perdidos = {equipo2.partPerdidos}")

def main():

    #Partido por jugar
    num_part = int(input("Ingrese el número de partidos a jugar: "))
    for i in range(num_part):
        print(f"\n--- Partido {i+1} ---")
        jugarPartido()
    ResultTorneo()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
