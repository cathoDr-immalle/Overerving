import math

class Shape:
    pass

class Cirkel(Shape):
    def __init__(self, straal):
        self.straal = straal
        self.opp = 0

    def oppervlakte(self):
        self.opp = self.straal * self.straal * math.pi

    def print(self):
        print(f"Een cirkel met als oppervlakte {self.opp}cm²")

class Vierkant(Shape):
    def __init__(self, zijde):
        self.zijde = zijde
        self.opp = 0

    def oppervlakte(self):
        self.opp = self.zijde * self.zijde

    def print(self):
        print(f"Een vierkant met als oppervlakte {self.opp}cm²")

if __name__ == "__main__":
    c = Cirkel(15)
    s = Cirkel(6)
    v = Vierkant(4)
    k = Vierkant(28)
    vormen = [c,s,v,k]
    for vorm in vormen:
        vorm.oppervlakte()
        vorm.print()