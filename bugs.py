"""Bug Hunt - Buginmetsästys

Yksinkertainen peli, jossa hahmo tutkii luolaa etsien bugeja. Kun hahmo (@)
ohjataan bugin (B) päälle, se hoitelee bugin, joka poistetaan pelistä. Lopuksi
kerrotaan montako bugia hoideltiin ja monellako siirrolla.

Luolassa erotellaan tutkitut (.) ja tutkimattomat (#) ruudut. Hahmoa siirretään
antamalla ilmansuunta (NESW). Luolan ulkopuolelle vieviä ilmansuuntia ei voi
antaa.

Pelin alussa käyttäjältä kysytään miten suuri luola tehdään ja montako bugia
sinne sijoitetaan. Luola on aina neliö, jossa on pysty- ja vaakasuunnassa
annettu määrä ruutuja.
"""

import random


class Luola:
    """Kuvaa neliön muotoisen luolan.

    :param koko: Kokonaisluku, luolan sivun pituus ruutuina.
    """

    OUTO = '#'
    TUTTU = '.'

    def __init__(self, koko):
        self.ruudut = []
        for x in range(koko):
            self.ruudut.append([self.OUTO] * koko)
        print("Luotiin {}x{} luola. Pidä hauskaa!\n".format(koko, koko))
        self.otukset = []

    # Puuttui indentation välilyönti, lisäsin 1 tab
    def tutki(self, x, y):
        """Merkitsee annetun ruudun ja sitä ympäröivät ruudut tutkituiksi."""
        for rivi in (y-1, y, y+1):
            if rivi < 0 or rivi >= len(self.ruudut):
                continue
            for sarake in (x-1, x, x+1):
                if sarake < 0 or sarake >= len(self.ruudut):
                    continue
                self.ruudut[rivi][sarake] = self.TUTTU

    def tulosta(self):
        """Tulostaa luolan tilanteen ruudulle."""
        for rivi in self.ruudut:
            for ruutu in rivi:
                print(ruutu, end='')
            print()

    def paivita(self):
        """Päivittää luolan otusten sijainnit."""
        for otus in self.otukset:
            # Oli vain 1 yhtäläisyysmerkki eli se koittaisi muutta muuttujan value. Lisäsin toisen merkin siihen (==), että se vertaileisi oikein.
            # Checkataan että otus.y < len(self.ruudut) niin ei tule IndexErroria!
            if otus.y < len(self.ruudut) and self.ruudut[otus.y][otus.x] == self.TUTTU:
                self.ruudut[otus.y][otus.x] = otus.MERKKI


# Puuttui kaksoispiste merkki (:) lopusta, lisäsin sen.
class Otus:
    """Kuvaa jotakin otusta, joka sijaitsee luolassa.

    Tämä on ns. abstrakti yläluokka, jonka muut luokat voivat periä. Tästä
    luokasta ei ole tarkoitus luoda olioita, vaan oliot luodaan näistä perivistä
    alaluokista.

    Luokan perivät luokat saavat käyttöönsä kaikki yläluokan ominaisuudet, mutta
    voivat lisäksi määritellä omia ominaisuuksiaan. Tällainen perintä kuuluu
    merkittäviin olio-ohjelmoinnin mahdollistamiin työkaluihin.
    """

    MERKKI = None

    def __init__(self):
        self.x = 0
        self.y = 0


class Hahmo(Otus):
    """Kuvaa hahmoa, pelimme sankaria.

    Hahmoa voidaan siirtää luolassa.

    :param nimi: Merkkijono, hahmon nimi.
    """

    MERKKI = '@'

    def __init__(self, nimi):
        Otus.__init__(self)
        self.nimi = nimi

    def liiku(self, dx, dy):
        """Siirtää olion sijaintia.

        :param dx: Kokonaisluku, sijainnin muutos vaakasuunnassa.
        :param dy: Kokonaisluku, sijainnin muutos pystysuunnassa.
        """
        if dx:
            self.x += dx
        if dy:
            # Piti korjata 'y' > 'dy'
            self.y += dy


class Bugi(Otus):
    """Kuvaa bugia, sankarimme metsästämää kohdetta.

    Bugi pysyy paikallaan pelin ajan.

    :param x: Kokonaisluku, bugin sijainti vaakasuunnassa.
    :param y: Kokonaisluku, bugin sijainti pystysuunnassa.
    """

    MERKKI = 'B'

    def __init__(self, x, y):
        Otus.__init__(self)
        self.x = x
        self.y = y


class Peli:
    """Mallintaa pelin, jossa itse toiminta tapahtuu.

    :param koko: Kokonaisluku, luolan sivun pituus.
    :param bugeja: Kokonaisluku, bugien määrä luolassa.
    """

    def __init__(self, koko, bugeja):
        # koko on string, korjasin errorin muuntamalla kokon integeriksi.
        self.koko = int(koko)
        self.luola = Luola(self.koko)
        # NameError, hahmoa ei ole olemassa vaan on Hahmo luokka, isolla kirjaimella.
        self.hahmo = Hahmo('foo')
        self.luola.otukset.append(self.hahmo)
        self.bugit = []
        # Vaihdoin 1 > 0, koska arrayt alkaa 0 ja ennen olisi ollut 1 vähemmän bugeja kuin pitäisi.
        for i in range(0, bugeja):
            bugi = self._luo_bugi()
            self.bugit.append(bugi)
            self.luola.otukset.append(bugi)
        # AttributeError: 'Peli' object has no attribute 'hamo'. Did you mean: 'hahmo'?
        # Vaihdoin 'hamo' sijaan 'hahmo'
        self.luola.tutki(self.hahmo.x, self.hahmo.y)

    def _luo_bugi(self):
        """Luo bugin, jonka sijainti on satunnainen tutkimaton luolan ruutu.

        return: Bugi, uusi bugi satunnaisessa sijainnissa.
        """
        # 'random' librarya ei ole importattu
        x = random.randint(1, self.koko - 1)
        y = random.randint(1, self.koko)
        return Bugi(x, y)

    def _luo_suunnat(self):
        """Luo listan liikesuunnista, jotka pitävät hahmon luolan sisällä.

        :return: Lista, mahdolliset liikesuunnat kirjaimin NESW.
        """
        suunnat = []
        if self.hahmo.y > 0:
            suunnat.append('N')
        if self.hahmo.x < self.koko - 1:
            suunnat.append('E')
        if self.hahmo.y < self.koko - 1:
            suunnat.append('S')
        if self.hahmo.x > 0:
            suunnat.append('W')

        # Funktio ei returnannut mitään, piti lisätä tämä.
        return suunnat

    def _kysy_suunta(self):
        """Kysyy käyttäjältä liikesuunnan.

        :return: Monikko, muutokset x- ja y-koordinaatteihin muodossa (dx, dy).
        """
        suunnat = self._luo_suunnat()
        # Puuttui stringin lopusta lainusmerkki ("), lisäsin sen
        print(suunnat)
        suunta = input("Valitse suunta({}):".format(''.join(suunnat)))
        if 'N' in suunnat and suunta in ('N', 'n'):
            return (0, -1)
        elif 'E' in suunnat and suunta in ('E', 'e'):
            return (1, 0)
        elif 'S' in suunnat and suunta in ('S', 's'):
            return (0, 1)
        elif 'W' in suunnat and suunta in ('W', 'w'):
            return (-1, 0)
        else:
            # Print ei ollut suljettu, lisäsin sulkumerkin loppuun
            print("Sallitut suunnat ovat ({}).\n".format(''.join(suunnat)))
            return self._kysy_suunta()

    def _debuggaa(self):
        """Poistaa bugin, jos hahmo on sen kohdalla.

        :return: True jos bugi poistettiin, muuten False.
        """
        for bugi in self.bugit:
            if bugi.x == self.hahmo.x:
                if bugi.y == self.hahmo.y:
                    self.bugit.pop(self.bugit.index(bugi))
                    self.luola.otukset.pop(self.luola.otukset.index(bugi))
                    return True
        return False

    def main(self):
        siirrot = 0
        bugit = 0
        while True:
            self.luola.paivita()
            self.luola.tulosta()
            if not self.bugit:
                break
            suunta = self._kysy_suunta()
            self.hahmo.liiku(*suunta)
            siirrot += 1
            self.luola.tutki(self.hahmo.x, self.hahmo.y)
            if self._debuggaa():
                bugit += 1
            print()

        print("\n\n*** {} bugia hoideltu {} siirrolla! ***\n\n".format(bugit,
                                                                       siirrot))


koko = input("Miten iso luola? ")
bugeja = int(input(f'Montako bugia?'))
peli = Peli(koko, bugeja)
peli.main()
