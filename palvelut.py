import random


class Asiakas:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.asiakasnro = self.luo_nro()

    def luo_nro(self):
        seg1 = f'{random.randint(0, 9)}{random.randint(0, 9)}'
        seg2 = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
        seg3 = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'

        nums = [seg1, seg2, seg3]
        return nums

    def set_nimi(self, nimi):
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")
        else:
            self.nimi = nimi

    def get_nimi(self):
        return self.nimi

    def set_ika(self, ika):
        if not ika:
            raise ValueError("Uusi ika on annettava.")
        else:
            self.ika = ika

    def get_ika(self):
        return self.ika

    def get_asiakasnumero(self):
        return f'xx-xxx-xxx'


class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.asiakkaat = []

    def luo_asiakasrivi(self, asiakas):
        return f'{asiakas.nimi} ({asiakas.asiakasnro[0]}-{asiakas.asiakasnro[1]}-{asiakas.asiakasnro[2]}) on {asiakas.ika}-vuotias.'

    def lisaa_asiakas(self, asiakas):
        if not asiakas:
            raise ValueError("Uusi asiakas on annettava.")
        else:
            self.asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        self.asiakkaat.append(asiakas)

    def tulosta_asiakkaat(self):
        print(f'Tuotteen {self.tuotenimi} asiakkaat ovat:')
        for asiakas in self.asiakkaat:
            print(self.luo_asiakasrivi(asiakas))
        print()


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, edu):
        self.edut.append(edu)

    def poista_etu(self, edu):
        if edu in self.edut:
            self.edut.remove(edu)

    def tulosta_edut(self):
        print(f'Tuotteen {self.tuotenimi} edut ovat:')
        for edu in self.edut:
            print(edu)
