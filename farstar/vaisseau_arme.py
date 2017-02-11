#-*- coding: utf-8 -*-
# Creation Date : 2017-02-03
# Created by : Antoine LeBel
from . import transportable

class VaisseauArme(transportable.Transportable):
    TYPE = "Vaisseau arme"
    CONSTRUCT = [int, int, int] #volume, masse, nombre max arme

    def __init__(self, nom, args):
        transportable.Transportable.__init__(self, nom)
        self.nb_max_arme = 0
        self.arme_equipe = []
        self.construire(args)

    def construire(self, args):
        if self.valide(args, self.CONSTRUCT):
            self._volume = args[0]
            self._masse = args[1]
            self.nb_max_arme = args[2]
        else:
            self.erreur_non_construction()

    def localiser(self, arme):
        if arme in self.arme_equipe:
            return self

    def peut_equiper(self, arme):
        return arme not in self.arme_equipe

    def equiper(self, arme):
        if arme not in self.arme_equipe:
            self.arme_equipe.append(arme)

    def desequiper(self, arme):
        if arme in self.arme_equipe:
            idx = self.arme_equipe.index(arme)
            del(self.arme_equipe[idx])
        else:
            print("Error : L'arme n'existe pas.")

    def get_masse(self):
        masse_arme = 0

        for arme in self.arme_equipe:
            masse_arme = masse_arme + arme.get_masse()

        return self._masse + masse_arme

    def get_volume(self):
        volume_arme = self._volume

        for arme in self.arme_equipe:
            volume_arme = volume_arme + arme.get_volume()

        return volume_arme

    def __str__(self):
        msg = transportable.Transportable.__str__(self)
        msg += "Armes équipées :\n"

        for arme in self.arme_equipe:
            msg += " - " + arme.get_nom() + "\n"

        return msg
