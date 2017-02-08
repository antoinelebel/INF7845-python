#-*- coding: utf-8 -*-
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
from . import phaser, vaisseau_arme_leger, usine_farstar
import re

class Farstart():

    def creer(self, nom_produit, *args):
        if self._valide_nom(nom_produit):
            produit = usine_farstar.UsineFarstar.creer_produit(nom_produit, *args)
            return produit

    def _valide_nom(self, nom_produit):
        return self._validation_regex(nom_produit) and self._validation_unique(nom_produit)

    def _validation_regex(self, nom_produit):
        return True

    def _validation_unique(self, nom_produit):
        return True

    def equiper(self, vaisseau, arme):
        if vaisseau.peut_equiper(arme):
            vaisseau.equiper(arme)
        else:
            print("Vous ne pouvez pas équiper " + arme.get_nom() + " sur " + vaisseau.get_nom())

    def desequiper(self, vaisseau, nom_arme):
        pass

    def localiser(self, nom_produit):
        pass

    def remplir_blaster(self, nom_blaster):
        pass
