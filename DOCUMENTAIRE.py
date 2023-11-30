import copy

class Documentaire:
    def __init__(self, _code, _titre, _date_sortie):
        self._code = _code
        self._titre = _titre
        self._date_sortie = _date_sortie

    def getcode(self):
        return self._code

    def gettitre(self):
        return self._titre

    def getdate_sortie(self):
        return self._date_sortie

    def setcode(self, newcode):
        self._code = newcode

    def settitre(self, newtitre):
        self._titre = newtitre

    def setdate_sortie(self, newdate_sortie):
        self._date_sortie = newdate_sortie

    def aff(self):
        print(f'code = {self.getcode()}')
        print(f'titre = {self.gettitre()}')
        print(f'date de sortie {self.getdate_sortie()}')

    def orr(self, Documentaire):
        code1, titre1, ds1 = self.getcode(), self.gettitre(), self.getdate_sortie()
        code2, titre2, ds2 = Documentaire.getcode(), Documentaire.gettitre(), Documentaire.getdate_sortie()

        if (code1 == code2) and (titre1 == titre2) and (ds1 == ds2):
            return "egale"
        else:
            return "n egale"

    def n_objet(self):
        pass

    def Tostring(self):
        pass


class Exemplaire(Documentaire):
    def __init__(self, _code, _titre, _date_sortie, _numero, _date_achat):
        super().__init__(_code, _titre, _date_sortie)
        self._numero = _numero
        self._date_achat = _date_achat

    def getnumero(self):
        return self._numero

    def getdate_achat(self):
        return self._date_achat

    def setnumero(self, newnumero):
        self._numero = newnumero

    def setdate_achat(self, newdate_achat):
        self._date_achat = newdate_achat

    def out(self):
        print(f'code = {self.getcode()}')
        print(f'titre = {self.gettitre()}')
        print(f'date de sortie {self.getdate_sortie()}')
        print(f"numero = {self.getnumero()}")
        print(f"date achat = {self.getdate_achat()}")

    def Tostring(self):
        pass


# Example of creating instances:
dc1 = Documentaire("001", "Title1", "2023-01-01")
ex1 = Exemplaire("001", "Title1", "2023-01-01", "A001", "2023-01-02")

# Example of calling methods:
dc1.aff()
ex1.out()
