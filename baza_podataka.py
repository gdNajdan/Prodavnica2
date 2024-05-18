class Prodavnica:
    def __init__(self, cena, kolicina, daonovac):
        self.cena=cena
        self.kolicina=kolicina
        self.daonovac=daonovac
    def Provera(self):
        if(self.daonovac>=self.cena*self.kolicina):
            return "kusur je ",self.daonovac-(self.cena*self.kolicina)
        else:
            return "niste dali dovoljno para"
ku1 = Prodavnica(120,3,500)
print(ku1.Provera())
