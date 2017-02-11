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
            self._volume = args[0] - args[2]
            self._masse = args[1]
            self._creer_soute(args[2], args[3])
        else:
            self.erreur_non_construction()

    def _creer_soute(self, volume_soute, masse_soute):
        self.soute = soute.Soute(volume_soute, masse_soute, self)

    def get_masse(self):
        return self._masse + self.soute.get_masse_courante()

    def get_volume(self):
        return self._volume + self.soute.get_capacite_volume()

    def get_volume_restant_soute(self):
        return self.soute.get_volume_restant()

    def get_element_soute(self):
        return self.soute.element_charges

    def _charger(self, element):
        self.soute.charger(element)

    def _decharger(self, nom_element):
        self.soute.decharger(nom_element)

    def _localiser(self, element):
        return self.soute.localiser(element)

    def peut_charger(self, element):
        return self.soute.peut_charger(element)

    def __str__(self):
        msg = transportable.Transportable.__str__(self)
        msg += "\nIl reste " + str(self.get_volume_restant_soute()) + " de volume dans la soute.\n"
        msg += "Chargement :\n"
        for element in self.soute.element_charges:
            msg += element.get_nom() + "\n"

        return msg + "\n"
