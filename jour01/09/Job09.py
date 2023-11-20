# pu : prix unitaire
# qs : quantitée de stock
# qa : quantitée achetée

# les '=+' '=-' etcs sont des opérateurs « combinés » qui effectuent des opérations et des affectations en une seule étape
# L'affectation est une instruction qui permet de modifier la valeur d'une variable


class Produit:
    def __init__(self, nom, pu, qs):
        self.nom = nom
        self.pu = pu
        self.qs = qs

    def afficher_informations(self):
        print(f"Produit: {self.nom}")
        print(f"Prix: {self.pu} €")
        print(f"En stock: {self.qs}")

    def mettre_a_jour_prix(self):
        self.pu *= qa

    def mettre_a_jour_stock(self, qa):
        if qa > 0:
            self.qs -= qa
            print(f"{qa} {self.nom}(s) ajouté(s) au stock.")
        else:
            print("Veuillez prendre vos pates SVP")

        if self.qs < 0:
            print(f"{self.qs} {self.nom} EN RUPTURE DE STOCK.")
        else:
            print("Choisisez votre payement...")


produit1 = Produit("pates", 1.55, 100)

print("Spaghetti 1kg:")
produit1.afficher_informations()

qa = int(input("Entrer la quantitée ici "))
produit1.mettre_a_jour_stock(qa)


produit1.mettre_a_jour_prix()

print("\nmise à jour infos:")
produit1.afficher_informations()
