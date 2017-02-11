#-*- coding: utf-8 -*-
# Creation Date : 2017-01-31
# Created by : Antoine LeBel
from farstar import farstar

FA = farstar.Farstart()
vaisseau_arme_leger1 = FA.creer("VC-1", [10, 50, 2])
phaser1 = FA.creer("PH-1", [1, 1])
phaser2 = FA.creer("PH-2", [1, 1])
phaser3 = FA.creer("PH-3", [1, 1])
phaser4 = FA.creer("PH-4", [1, 1])

blaster1 = FA.creer("BL-1", [2, 2, 100, 50])
blaster2 = FA.creer("BL-2", [2, 2, 100, 50])

transport1 = FA.creer("VT-2", [100, 100, 90, 300])

hybride1 = FA.creer("MR-1", [200, 150, 5, 180, 600])

conteneur1 = FA.creer("CT-1", [1,1])
conteneur2 = FA.creer("CT-2", [1,1])
conteneur3 = FA.creer("CT-3", [1,1])
conteneur4 = FA.creer("CT-4", [1,1])
conteneur5 = FA.creer("CT-5", [1,1])
conteneur6 = FA.creer("CT-6", [10,100])
conteneur7 = FA.creer("CT-7", [10,100])
conteneur8 = FA.creer("CT-8", [10,100])
conteneur9 = FA.creer("CT-9", [10,100])

FA.equiper(vaisseau_arme_leger1, phaser1)
FA.equiper(vaisseau_arme_leger1, phaser2)

FA.charger(transport1, conteneur1)
FA.charger(transport1, conteneur2)
FA.charger(transport1, conteneur3)
FA.charger(transport1, conteneur4)
FA.charger(transport1, conteneur5)

FA.charger(transport1, vaisseau_arme_leger1)
FA.desequiper(vaisseau_arme_leger1, phaser2)
FA.charger(transport1, phaser2)

FA.equiper(hybride1, blaster1)
FA.equiper(hybride1, blaster2)
FA.equiper(hybride1, phaser3)
FA.equiper(hybride1, phaser4)
print(hybride1)

FA.charger(hybride1, conteneur6)
FA.charger(hybride1, conteneur7)
FA.charger(hybride1, conteneur8)
FA.charger(hybride1, conteneur9)
FA.charger(hybride1, transport1)
# print(transport1)
print(hybride1)
# print(vaisseau_arme_leger1)

# FA.localiser(phaser1)
# FA.localiser(phaser2)
# FA.localiser(phaser3)
# FA.localiser(phaser4)

# print(blaster1)
# FA.remplir_blaster("BL-1")
# print(blaster1)
