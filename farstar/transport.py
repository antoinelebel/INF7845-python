#-*- coding: utf-8 -*-
# Creation Date : 2017-02-05
# Created by : Antoine LeBel
from . import transportable, soute

class Transport(transportable.Transportable):
    TYPE = "Transport"
    CONSTRUCT = [int, int, int, int]

    def __init__(self, nom, args):
        transportable.Transportable.__init__(self, nom)
        self.soute = None
        self.construire(args)

    def construire(self, args):
        if self.valide(args, self.CONSTRUCT):
            self._volume = args[0]
            self._masse = args[1]
            self._creer_soute(args[2], args[3])
        else:
            self.erreur_non_construction();

    def _creer_soute(self, volume_soute, masse_soute):
        self.soute = soute.Soute(volume_soute, masse_soute, self)

    def get_masse(self):
        return transportable.Transportable.get_masse(self) + self.soute.get_masse_courante()

    def get_volume(self):
        return transportable.Transportable.get_volume(self) + self.soute.get_capacite_volume()

    def get_volume_restant_soute(self):
        return self.soute.get_volume_restant()

    def get_element_soute(self):
        return self.soute.element_charges

    def charger(self, element):
        self.soute.charger(element)

    def decharger(self, nom_element):
        self.soute.decharger(nom_element)

    def localiser(self, element):
        return self.soute.localiser(element)

    def __str__(self):
         return "Masse : " + str(self.get_masse())
