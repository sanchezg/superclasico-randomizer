# To change this template, choose Tools | Templates
# and open the template in the editor.
import random

__author__="gonzalo"
__date__ ="$11/09/2011 12:14:40$"

listaCompleta = {
   'Jugador1': 7.85,
   'Jugador2': 6.2,
   'Jugador3': 3.1,
   'Jugador4': 8.45,
   'Jugador5': 6.11,
   'Jugador6': 7.63,
   'Jugador7': 6.12,
   'Jugador8': 8.64,
   'Jugador9': 6.52,
   'Jugador10': 1.25
}

def sel_aleatoria():
    jug_aleat = jugador()
    jug_aleat.nombre, jug_aleat.promedio = random.choice(listaCompleta.items())
    del listaCompleta[jug_aleat.nombre]
    return jug_aleat

def minimus(jug1, jug2):
    if jug1.promedio < jug2.promedio:
        return jug1
    else:
        return jug2

def maximus(jug1, jug2):
    if jug1.promedio > jug2.promedio:
        return jug1
    else:
        return jug2

def agregar_jugadores(equipo1, equipo2, jug1, jug2):
    #Not implemented
    print None
    #if equipo1.promedio > equipo2.promedio:
    #    if equipo1.punt_arq > equipo2.punt_arq and jug1.arquero > jug2.arquero:

class equipo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.promedio = 0
        self.jugadores = {}
    def recalcular(self):
        for jug in self.jugadores:
            self.promedio = self.promedio + self.jugadores[jug]
        #self.puntaje_habilidades()
    def agregar(self, jugador):
        self.jugadores[jugador.nombre] = jugador.promedio
    #def puntaje_habilidades(self):
    #    for jug in self.jugadores:
    #        self.punt_arq = self.punt_arq + self.jugadores[jug].arquero
    #        self.punt_def = self.punt_def + self.jugadores[jug].defensor
    #        self.punt_vol = self.punt_vol + self.jugadores[jug].volante
    #        self.punt_del = self.punt_del + self.jugadores[jug].delantero
    def print_jugadores(self):
        print 'Lista de %s' %self.nombre
        print 'Puntaje total: %s' %self.promedio
        print self.jugadores.keys()

class jugador():
    def __init__(self, nombre='NN', promedio='0'):
        self.nombre = nombre
        self.promedio = promedio
    def set_habilidades(self, arquero, defensor, volante, delantero):
        self.arquero = arquero
        self.defensor = defensor
        self.volante = volante
        self.delantero = delantero

if __name__ == "__main__":
    equipo1 = equipo('SeguidoresDelMaestroAmor')
    equipo2 = equipo('LigaDeAmosDeCasaResentidos')
    equipo1.agregar(sel_aleatoria())
    equipo2.agregar(sel_aleatoria())
    while listaCompleta != {}:
        equipo1.recalcular()
        equipo2.recalcular()
        jug1=sel_aleatoria()
        jug2=sel_aleatoria()
        if equipo1.promedio > equipo2.promedio:
            equipo1.agregar(minimus(jug1, jug2))
            equipo2.agregar(maximus(jug1, jug2))
        else:
            equipo1.agregar(maximus(jug1, jug2))
            equipo2.agregar(minimus(jug1, jug2))
    equipo1.print_jugadores()
    equipo2.print_jugadores()
