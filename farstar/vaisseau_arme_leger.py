#-*- coding: utf-8 -*-
# Creation Date : 2017-02-05
# Created by : Antoine LeBel
from . import vaisseau_arme
from .phaser import Phaser

class VaisseauArmeLeger(vaisseau_arme.VaisseauArme):
    TYPE = "Vaisseau Armé Léger"

    def __init__(self, nom, args):
        vaisseau_arme.VaisseauArme.__init__(self, nom, args)

    def equiper(self, arme):
        if self.peut_equiper(arme):
            self.arme_equipe.append(arme)
        else:
            print("Erreur : Problème d'équipement")

    def peut_equiper(self, arme):
        result = super(VaisseauArmeLeger, self).peut_equiper(arme)

        if result and isinstance(arme, Phaser):
            return True
        else:
            return False
