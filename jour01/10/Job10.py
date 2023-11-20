# exemple sur un capital de depart minimum d'une SA : 37K€

# utiliser des abreviations permet d'aller plus vite
# tra : taux de rendement annuel
# mi : montant initial
# mf : montant final


class SimulationInvestissement:

    # '__init__' sert à attribuer à chaque objet de la classe une valeur d'attribut qui lui est propre.
    # "self" est relié a "__init__"

    def __init__(self, mi, tra):
        self.mi = mi
        self.tra = tra

    def gain_annuel(self):
        gain_annuel = (self.tra / 100) * self.mi
        return gain_annuel

    def augmenter_capital(self, augmentation, augmentation_taux):
        self.mi += augmentation
        self.tra += augmentation_taux

    def retirer_capital(self, pourcentage_retrait, diminution_taux):
        retrait = pourcentage_retrait / 100 * self.mi
        self.mi -= retrait
        self.tra -= diminution_taux


mi = 37000
tra = 6

simulation = SimulationInvestissement(mi, tra)

#gain annuel
gain_annuel_initial = simulation.gain_annuel()
print(f"Gain annuel: {gain_annuel_initial} euros")

# "L’investisseur augmente son capital de 5 000 euros, le taux augmenta de 2%

simulation.augmenter_capital(5000, 2)
nouveau_gain_annuel = simulation.gain_annuel()
print(f"\nNouveau gain annuel après augmentation : {nouveau_gain_annuel} euros")


# "L'investisseur retire 10% ,suite à ce retrait le rendement diminue de 1%"

simulation.retirer_capital(10, 1)
mf = simulation.mi + simulation.gain_annuel()
print(f"\nResultat après retrait : {mf} euros")