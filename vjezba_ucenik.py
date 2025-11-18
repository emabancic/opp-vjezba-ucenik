class Ucenik:
    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []

    def dodaj_ocjenu(self, ocjena):
        self.ocjene.append(ocjena)

    def izracunaj_prosjek(self):
        if len(self.ocjene) == 0:
            return 0.0
        return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        prosjek = self.izracunaj_prosjek()
        print("Učenik:", self.ime, self.prezime)
        print("Razred:", self.razred)
        print("Ocjene:", self.ocjene)
        print("Prosjek:", f"{prosjek:.2f}")
        print("-------------------------")


# Glavni dio programa
u1 = Ucenik("Marko", "Horvat", "7.b")
u2 = Ucenik("Ana", "Kovač", "6.a")

# Dodavanje ocjena
u1.dodaj_ocjenu(5)
u1.dodaj_ocjenu(4)
u2.dodaj_ocjenu(3)
u2.dodaj_ocjenu(5)

# Ispis informacija
u1.info()
u2.info()
