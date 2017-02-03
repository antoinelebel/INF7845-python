#-*- coding: utf-8 -*-
# Creation Date : 2017-02-03
# Created by : Antoine LeBel
from . import transportable
class VaisseauArme(transportable.Transportable):
    TYPE = "ABSVaisseau"
    CONSTRUCT = [int, int, int] #volume, masse, nombre max arme

    def __init__(self, nom):
        transportable.Transportable(nom, volume, masse)
        self.nb_max_arme = None
        self.arme_equipe = []

    def construire(*args):
        if self.valide(args, self.CONSTRUCT):
            self._volume = args[0]
            self._masse = args[0]
            self._nb_max_arme = args[0]
        else:
            raise nonConstructionErreur("Le vaisseau arme " + self.TYPE + " ne peut être construit")

    def localiser(self, produit):
        pass

    def equiper(self, arme):
        pass

    def desequiper(self, nom_arme):
        pass

    def get_masse(self):
        pass

    def get_volume(self):
        pass

    def __str__(self):
        msg = transportable.Transportable.__str__()
        msg = msg + "meeh"
        return msg
