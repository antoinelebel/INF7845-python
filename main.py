#-*- coding: utf-8 -*-
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
from farstar import farstar

fs = farstar.Farstart()
vaisseau_leger_1 = fs.creer("VC-1", [4, 4, 1])
vaisseau_leger_2 = fs.creer("VC-2", [1, 1, 1])
vaisseau_lourd_1 = fs.creer("VL-1", [3, 3, 3])
phaser1 = fs.creer("PH-1", [1,1])
blaster1 = fs.creer("BL-1", [2,2, 100, 50])

fs.equiper(vaisseau_leger_1, phaser1)

vaisseau_tr_1 = fs.creer("VT-1", [1, 1, 4, 4])
vaisseau_tr_1.charger(vaisseau_leger_1)
fs.desequiper(vaisseau_leger_1, "PH-1")
vaisseau_tr_1.charger(vaisseau_leger_1)

# print(vaisseau_leger_1.arme_equipe)

# print(vaisseau_leger_1.arme_equipe)
fs.equiper(vaisseau_leger_1, blaster1)
fs.equiper(vaisseau_lourd_1, blaster1)

# print(vaisseau_leger_1.arme_equipe)
# print(vaisseau_lourd_1.arme_equipe)

print(vaisseau_leger_1.get_nom())
