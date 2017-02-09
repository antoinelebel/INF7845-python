#-*- coding: utf-8 -*-
# Creation Date : 2017-02-02
# Created by : Antoine LeBel
class Soute():

    def __init__(self, cap_masse, cap_volume, parent):
        self.cap_masse = cap_masse
        self.cap_volume = cap_volume
        self._parent = parent
        self.element_charges = []
        #TODO get DB manager

    def get_capacite_masse(self):
        return self.cap_masse

    def get_capacite_volume(self):
        return self.cap_volume

    def get_masse_courante(self):
        charge = 0

        for elem in self.element_charges:
            charge = charge + elem.get_masse()

        return charge

    def get_volume_restant(self):
        volume = self.get_capacite_volume()

        for elem in self.element_charges:
            volume = volume - elem.get_volume()

        return volume

    def peut_charger(self, produit):
        masse_potentielle = self.get_masse_courante() + produit.get_masse()
        volume_potentiel_restant = self.get_volume_restant() - produit.get_volume()

        if masse_potentielle > self.get_capacite_masse():
            print("Erreur : La capacité de la masse de la soute {} dépassée".format(self._parent.get_nom()))
            return False

        if volume_potentiel_restant < 0:
            print("Erreur : La capacité du volume de la soute {} dépassée".format(self._parent.get_nom()))
            return False

        return True

    def charger(self, produit):
        if self.peut_charger(produit):
            self.element_charges.append(produit)

    def decharger(self, nom_produit):
        if nom_produit in self._get_liste_nom_produit():
            produit = self._get_produit_par_nom(nom_produit)
            self.element_charges.remove(produit)
        else:
            print("Erreur : Impossible de décharger.")

    def localiser(self, nom_produit):
        pass

    def _get_liste_nom_produit(self):
        return [p.get_nom() for p in self.element_charges]

    def _get_produit_par_nom(self, nom_produit):
        for p in self.element_charges:
            if p.get_nom() == nom_produit:
                return p
