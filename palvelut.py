class Asiakas:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.asiakasnro = self.luo_nro()

    def luo_nro():
        pass


class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.asiakkaat = []

    def luo_asiakasrivi(Asiakas):
        pass

    def lisaa_asiakas(Asiakas):
        pass

    def poista_asiakas(Asiakas):
        pass

    def tulosta_asiakkaat():
        pass


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
