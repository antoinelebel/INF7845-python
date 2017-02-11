#-*- coding: utf-8 -*-
# Creation Date : 2017-02-11
# Created by : Antoine LeBel
from . import transport, vaisseau_arme

class Hybride(transport.Transport, vaisseau_arme.VaisseauArme):
    TYPE = "Hybride"
    CONSTRUCT = [int, int, int, int, int]

    def __init__(self, nom, args):
        transport.Transport.__init__(self, nom, args)
        vaisseau_arme.VaisseauArme.__init__(self, nom, args)
        self.construire(args)

    def construire(self, args):
        if self.valide(args, self.CONSTRUCT):
            self._volume = args[0] - args[3]
            self._masse = args[1]
            self.nb_max_arme = args[2]
            self._creer_soute(args[3], args[4])
        else:
            self.erreur_non_construction()

    def get_masse(self):
        return vaisseau_arme.VaisseauArme.get_masse(self) + self.soute.get_masse_courante()

    def get_volume(self):
        return vaisseau_arme.VaisseauArme.get_volume(self) + self.soute.get_capacite_volume()

    def localiser(self, element):
        pass

    def __str__(self):
        msg = vaisseau_arme.VaisseauArme.__str__(self)
        msg += "\nIl reste " + str(self.get_volume_restant_soute()) + " de volume dans la soute.\n"
        msg += "Chargement :\n"
        for element in self.soute.element_charges:
            msg += element.get_nom() + "\n"

        return msg + "\n"
