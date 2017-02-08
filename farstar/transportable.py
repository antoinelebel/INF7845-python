#-*- coding: utf-8 -*-
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
from .exception import nonConstructionException
class Transportable():
    TYPE = "ABS"

    def __init__(self, nom):
        self._nom = nom
        self._masse = None
        self._volume = None

    def construire(self, args):
        raise NotImplementedError("Class needs to implement {} :".format(self.__class__.__name__))

    def valide(self, args, validations):
        return self._valide_args(args, validations) and self._match_type(args, validations)
    def _valide_args(self, args, validations):
        return len(args) == len(validations)

    def _match_type(self, args, validations):
        for i in range(0, len(args) - 1):
            if type(args[i]) != validations[i]:
                return False

        return True

    def erreur_non_construction(self, msg=None):
        if not msg:
            msg = "Erreur : Vous ne pouvez pas construire " + self.TYPE + " arguments invalides. Besoin : " + " ".join(map(str, self.CONSTRUCT))
        raise nonConstructionException(msg)

    def get_nom(self):
        return self._nom

    def get_masse(self):
        return self._masse

    def get_volume(self):
        return self._volume

    def __str__(self):
        return "Caractéristique de " + self.getNom() + "\nType : " + self.TYPE + "\n"

