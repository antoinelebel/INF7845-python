#-- coding: utf-8 --
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
class UsineFarstar():
    @staticmethod
    def creer_produit(nom, args):
        type_produit = nom[0:2]

        if type_produit == "VT":
            return Transport(nom, args)
        if type_produit == "MR":
            return Hybride(nom, args)
        if type_produit == "VC":
            return VaisseauArmeLeger(nom, args)
        if type_produit == "VL":
            return VaisseauArmeLourd(nom, args)
        if type_produit == "PH":
            return Phaser(nom, args)
        if type_produit == "BL":
            return Blaster(nom, args)
        if type_produit == "CT":
            return Conteneur(nom, args)

        raise nonConstructionException("Ce type de produit n'existe pas.")
