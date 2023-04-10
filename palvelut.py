class Asiakas:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.asiakasnro = self.luo_nro()

    def luo_nro(self):
        pass

    def set_nimi(self, nimi):
        if nimi == False:
            raise ValueError("Anna uusi nimi!")
        else:
            self.nimi = nimi

    def get_nimi(self):
        return self.nimi

    def set_ika(self, ika):
        if ika == False:
            raise ValueError("Anna uusi ika!")
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
        return f'{asiakas.nimi} ({asiakas.asiakasnro}) on {asiakas.ika}-vuotias.'

    def lisaa_asiakas(self, asiakas):
        self.asiakkaat += asiakas

    def poista_asiakas(self, asiakas):
        self.asiakkaat -= asiakas

    def tulosta_asiakkaat(self):
        for asiakas in self.asiakkaat:
            print(self.luo_asiakasrivi(asiakas))


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(str):
        pass

    def poista_etu(str):
        pass

    def tulosta_edut():
        pass


# Testit
asiakas = Asiakas("jeps", 104)
asiakas.set_nimi(False)
