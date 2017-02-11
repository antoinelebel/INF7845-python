#-*- coding: utf-8 -*-
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
from . import phaser, vaisseau_arme_leger, usine_farstar, manager
import re

class Farstart():

    def __init__(self):
        self.manager = manager.Manager()

    def creer(self, nom_produit, args):
        if self._valide_nom(nom_produit):
            produit = usine_farstar.UsineFarstar.creer_produit(nom_produit, args)
            self.manager.ajouter_produit(produit)
            return produit

    def _valide_nom(self, nom_produit):
        return self._validation_regex(nom_produit) and self._validation_unique(nom_produit)

    def _validation_regex(self, nom_produit):
        return True

    def _validation_unique(self, nom_produit):
        return True

    def charger(self, vaisseau, produit):
        if self.manager.is_produit_disponible(produit) and vaisseau.peut_charger(produit):
            vaisseau._charger(produit)
            self.manager.ajouter_produit_placer(produit)
        else:
            print("Vous ne pouvez pas charger " + produit.get_nom() + " sur " + vaisseau.get_nom())

    def decharger(self, vaisseau, nom_produit):
        vaisseau._decharger(nom_produit)
        self.manager.retirer_produit_placer(nom_produit)

    def equiper(self, vaisseau, arme):
        if self.manager.is_produit_disponible(arme) and vaisseau.peut_equiper(arme):
            vaisseau.equiper(arme)
            self.manager.ajouter_produit_placer(arme)
        else:
            print("Vous ne pouvez pas équiper " + arme.get_nom() + " sur " + vaisseau.get_nom())

    def desequiper(self, vaisseau, nom_arme):
        vaisseau.desequiper(nom_arme)
        self.manager.retirer_produit_placer(nom_arme)

    def localiser(self, nom_produit):
        pass

    def remplir_blaster(self, nom_blaster):
        blaster = self.manager.produit_cree[nom_blaster]
        print("TODO remplir" + blaster)
