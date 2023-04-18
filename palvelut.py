import random


class Asiakas:
    """
    Konstruktori ottaa 2 args: nimi, ika

    Asiakas luokka
    - nimi (str): asiakkaan nimi.
    - ika (int): asiakkaan ikä.
    - asiakasnro (lista): kolmen merkkijonon luettelo

    Metodit:
    - luo_nro(): Luo uuden asiakasnumeron.
    - set_nimi(nimi: string): Asettaa asiakkaan nimen.
    - get_nimi(): Hakee asiakkaan nimen.
    - set_ika(ika: int): Asettaa asiakkaan iän.
    - get_ika(): Hakee asiakkaan iän.
    - get_asiakasnumero(): Palauttaa asiakasnumeroa edustavan merkkijonon.
    """

    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__ika = ika
        self.__asiakasnro = self._luo_nro()

    def _luo_nro(self):
        seg1 = f'{random.randint(0, 9)}{random.randint(0, 9)}'
        seg2 = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
        seg3 = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'

        nums = [seg1, seg2, seg3]
        return nums

    def set_nimi(self, nimi):
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")
        else:
            self.__nimi = nimi

    def get_nimi(self):
        return self.__nimi

    def set_ika(self, ika):
        if not ika:
            raise ValueError("Uusi ika on annettava.")
        else:
            self.__ika = ika

    def get_ika(self):
        return self.__ika

    def get_asiakasnumero(self):
        nro = self.__asiakasnro
        return f'{nro[0]}-{nro[1]}-{nro[2]}'


class Palvelu:
    """
    Konstruktori ottaa 1 argumentin: tuotenimi

    Palvelu luokka
    - tuotenimi (str): Tuotteen nimi.
    - asiakkaat (lista): Lista Asiakas-olioita.

    Metodit:
    - luo_asiakasrivi(asiakas): Luo asiakkaasta muotoiltun merkkijonon, jossa on hänen nimi, asiakasnumero ja ikä.
    - lisaa_asiakas(asiakas): Lisää uuden Asiakas-olion asiakkaat listaan.
    - poista_asiakas(asiakas): Poistaa Asiakas-olion asiakkaat listasta.
    - tulosta_asiakkaat(): Tulostaa listan tämän palvelun asiakkaista.
    """

    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(self, asiakas):
        nro = asiakas.get_asiakasnumero()
        return f'{asiakas.get_nimi()} ({nro}) on {asiakas.get_ika()}-vuotias.'

    def lisaa_asiakas(self, asiakas):
        if not asiakas:
            raise ValueError("Uusi asiakas on annettava.")
        else:
            self.__asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        self.asiakkaat.append(asiakas)

    def tulosta_asiakkaat(self):
        print(f'Tuotteen {self.tuotenimi} asiakkaat ovat:')
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakasrivi(asiakas))
        print()


class ParempiPalvelu(Palvelu):
    """
    Konstruktori ottaa 1 argumentin: tuotenimi

    ParempiPalvelu luokka
    - tuotenimi (str): Tuotteen nimi.
    - asiakkaat (lista): Lista Asiakas-olioita.
    - edut (lista): Palvelun edut.

    Metodit:
    - lisaa_etu(self, edu): Lisää uuden edun tähän palveluun.
    - poista_etu(self, edu): Poistaa edun tästä palvelusta.
    - tulosta_edut(self): Tulostaa tämän palvelun edut.
    """

    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, edu):
        self.__edut.append(edu)

    def poista_etu(self, edu):
        if edu in self.__edut:
            self.__edut.remove(edu)

    def tulosta_edut(self):
        print(f'Tuotteen {self.tuotenimi} edut ovat:')
        for edu in self.__edut:
            print(edu)
