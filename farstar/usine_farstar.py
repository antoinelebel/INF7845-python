#-- coding: utf-8 --
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
from . import phaser, vaisseau_arme_leger, blaster, vaisseau_arme, transport, conteneur, hybride

class UsineFarstar():
    @staticmethod
    def creer_produit(nom, args):
        type_produit = nom[0:2]

        if type_produit == "VT":
            return transport.Transport(nom, args)
        if type_produit == "MR":
            return hybride.Hybride(nom, args)
        if type_produit == "VC":
            return vaisseau_arme_leger.VaisseauArmeLeger(nom, args)
        if type_produit == "VL":
            return vaisseau_arme.VaisseauArme(nom, args)
        if type_produit == "PH":
            return phaser.Phaser(nom, args)
        if type_produit == "BL":
            return blaster.Blaster(nom, args)
        if type_produit == "CT":
            return conteneur.Conteneur(nom, args)

        raise nonConstructionException("Ce type de produit n'existe pas.")
