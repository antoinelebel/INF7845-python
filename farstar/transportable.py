#-*- coding: utf-8 -*-
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
class Transportable():
    TYPE = ""

    def __init__(self, nom):
        self.nom = nom

    def construire(self):
        raise NotImplementedError("Class needs to implement {} :".format(self.__class__.__name__))

    def _valide_args(self, args, validations):
        pass

    def _match_type(self, args, validations):
        pass

    def erreur_non_construction(self, msg=None):
        if not msg:
            msg = "Erreur : Vous ne pouvez pas construire " + self.TYPE + " arguments invalides."
        raise nonConstructionException(msg)
