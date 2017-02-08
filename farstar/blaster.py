#-*- coding: utf-8 -*-
# Creation Date : 2017-02-05
# Created by : Antoine LeBel
from . import transportable
from .exception import nonConstructionException

class Blaster(transportable.Transportable):
    TYPE = "Blaster"
    CONSTRUCT = [int, int, int, int]

    def __init__(self, nom, args):
        transportable.Transportable.__init__(self, nom)
        self._capacite_gaz = 0
        self._gaz_courant = 0
        self.construire(args)

    def construire(self, args):
        if self.valide(args, self.CONSTRUCT):
            self._volume = args[0]
            self._masse = args[1]
            self._set_gaz(args[2], args[3])
        else:
            self.erreur_non_construction();

    def _set_gaz(self, capacite_gaz, gaz_courant):
        if gaz_courant > capacite_gaz:
            raise nonConstructionException("Le gaz courant est supérieur à la capacité lors de la création de " + self.get_nom())

        self._capacite_gaz = capacite_gaz
        self._gaz_courant = gaz_courant

