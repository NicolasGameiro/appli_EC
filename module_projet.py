class Projet():
    def __init__(self, name):
        self.name = name
        self.list_calcul = []

    def get_calcul(self):
        return self.list_calcul

    def add_calcul(self, calcul):
        self.list_calcul.append(calcul)
        return

class Calcul():
    def __init__(self,name, type):
        self.name = name
        self.type = type # poutre, ferme, composant,...


def test():
    projet_maule = Projet("maule")

    print(projet_maule.name)

    arba = Calcul("arba_centrale", "arba")
    solive = Calcul("solive", "solive")

    projet_maule.add_calcul(arba)
    projet_maule.add_calcul(solive)

    L = projet_maule.get_calcul()

    for calcul in L:
        print(calcul.name)

if __name__ == "__main__":
    test()