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
        return cap_masse

    def get_capacite_volume(self):
        return cap_volume

    def get_masse_courant(self):
        pass

    def get_volume_restant(self):
        pass

    def peut_charger(self):
        pass

    def charger(self, produit):
        pass

    def decharger(self, nom_produit):
        pass

    def localiser(self, nom_produit):
        pass
