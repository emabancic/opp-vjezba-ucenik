# -----------------------------------------
# 1. Roditeljska klasa Vozilo
# -----------------------------------------
class Vozilo:
    def __init__(self, marka, model, godina_proizvodnje, cijena):
        self.marka = marka
        self.model = model
        self.godina = godina_proizvodnje
        self.cijena = cijena

    def info(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina: {self.godina}, Cijena: {self.cijena} EUR")

    def promijeni_cijenu(self, nova_cijena):
        self.cijena = nova_cijena
        print(f"Cijena je uspješno promijenjena na {self.cijena} EUR")


# -----------------------------------------
# 2. Izvedena klasa ElektricnoVozilo
# -----------------------------------------
class ElektricnoVozilo(Vozilo):
    def __init__(self, marka, model, godina_proizvodnje, cijena, domet_baterije):
        super().__init__(marka, model, godina_proizvodnje, cijena)
        self.domet_baterije = domet_baterije

    def info(self):
        super().info()
        print(f"Domet baterije: {self.domet_baterije} km")


# -----------------------------------------
# 3. Pomoćne funkcije
# -----------------------------------------
def ispisi_izbornik():
    print("\n--- AUTOSALON v2.0 ---")
    print("1. Dodaj novo (obično) vozilo")
    print("2. Dodaj novo (električno) vozilo")
    print("3. Ispiši podatke o određenom vozilu")
    print("4. Promijeni cijenu vozilu")
    print("5. Ispiši sva vozila")
    print("0. Izlaz")
    print("----------------------")


def unosVozila():
    marka = input("Unesite marku: ")
    model = input("Unesite model: ")
    godina = int(input("Godina proizvodnje: "))
    cijena = float(input("Cijena (EUR): "))
    return Vozilo(marka, model, godina, cijena)


def unosElVozila():
    marka = input("Unesite marku: ")
    model = input("Unesite model: ")
    godina = int(input("Godina proizvodnje: "))
    cijena = float(input("Cijena (EUR): "))
    domet = int(input("Domet baterije (km): "))
    return ElektricnoVozilo(marka, model, godina, cijena, domet)


def pronadji_vozilo(lista_vozila):
    marka = input("Upišite marku vozila: ")
    model = input("Upišite model vozila: ")

    for vozilo in lista_vozila:
        if vozilo.marka == marka and vozilo.model == model:
            return vozilo
    
    print("Vozilo nije pronađeno.")
    return None


# -----------------------------------------
# 4. Glavni program
# -----------------------------------------
autosalon = []

while True:
    ispisi_izbornik()
    try:
        izbor = int(input("Odaberite opciju: "))

        if izbor == 1:
            print("Dodavanje običnog vozila:")
            voz = unosVozila()
            autosalon.append(voz)

        elif izbor == 2:
            print("Dodavanje električnog vozila:")
            voz = unosElVozila()
            autosalon.append(voz)

        elif izbor == 3:
            print("Pretraga vozila:")
            voz = pronadji_vozilo(autosalon)
            if voz:
                voz.info()

        elif izbor == 4:
            print("Promjena cijene vozila:")
            voz = pronadji_vozilo(autosalon)
            if voz:
                nova = float(input("Unesite novu cijenu: "))
                voz.promijeni_cijenu(nova)

        elif izbor == 5:
            print("\n--- SVA VOZILA U AUTOSALONU ---")
            for voz in autosalon:
                voz.info()
                print()

        elif izbor == 0:
            print("Hvala na korištenju programa!")
            break

        else:
            print("Neispravan izbor!")

    except ValueError:
        print("Greška! Unesite brojčanu vrijednost.")
