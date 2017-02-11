#-*- coding: utf-8 -*-
# Creation Date : 2017-02-08
# Created by : Antoine LeBel
from .transport import Transport
from .vaisseau_arme import VaisseauArme

class Manager():

    def __init__(self):
        self.produit_cree = {}
        self.produit_place = {}

    def ajouter_produit(self, produit):
        if produit.get_nom() not in self.produit_cree:
            self.produit_cree[produit.get_nom()] = produit
        else:
            print("Erreur : {} est déjà créé".format(produit.get_nom()))

    def ajouter_produit_placer(self, produit):
        if produit.get_nom() not in self.produit_place:
            self.produit_place[produit.get_nom()] = produit
        else:
            print("Erreur : {} est déjà placé.".format(produit.get_nom()))

    def retirer_produit_placer(self, produit):
        self.produit_place.pop(produit.get_nom())

    def is_produit_disponible(self, produit):
        if produit.get_nom() not in self.produit_cree:
            print("Erreur : {} n'est pas créé.".format(produit.get_nom()))
            return False

        if produit.get_nom() in self.produit_place:
            print("Erreur : {} est déjà placé.".format(produit.get_nom()))
            return False

        return True

    def get_liste_vaisseau(self):
        liste_vaisseau = []

        for element in self.produit_cree:
            if isinstance(self.produit_cree[element], Transport) or isinstance(self.produit_cree[element], VaisseauArme):
                liste_vaisseau.append(self.produit_cree[element])

        return liste_vaisseau
