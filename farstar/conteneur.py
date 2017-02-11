#-*- coding: utf-8 -*-
# Creation Date : 2017-02-11
# Created by : Antoine LeBel
from . import transportable

class Conteneur(transportable.Transportable):
    TYPE = "Container"
    CONSTRUCT = [int, int]

    def __init__(self, nom, args):
        transportable.Transportable.__init__(self, nom)
        self.construire(args)

    def construire(self, args):
        if self.valide(args, self.CONSTRUCT):
            self._volume = args[0]
            self._masse =args[1]
        else:
            self.erreur_non_construction()
