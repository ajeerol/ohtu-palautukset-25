import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    """
    Luetaan pelaajatiedot listalta
    """

    def get_players(self):
        """
        Kovakoodattu pelaajalista
        """
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    """
    Testiluokka StatisticsService-luokalle
    """
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsi_pelaaja(self):
        """
        Testataan search-metodia
        """

        nimi1 = "Semenko"

        # haetaan tietyn pelaajan tiedot
        pelaaja1 = self.stats.search(nimi1)

        self.assertEqual(str(pelaaja1), "Semenko EDM 4 + 12 = 16")

        nimi2 = "PelaajaaEiLoydy"
        pelaaja2 = self.stats.search(nimi2)

        self.assertEqual(str(pelaaja2), 'None')
        
    def test_nayta_joukkue(self):
        """
        Testataan team-metodia
        """

        joukkue_nimi = "EDM"
        pelaaja_nimi= "Semenko"

        pelaaja = self.stats.search(pelaaja_nimi)

        joukkue = self.stats.team(joukkue_nimi)

        # Löytyykö pelaaja joukkueesta
        self.assertIn(pelaaja,joukkue)

    def test_nayta_top_lista(self):
        """
        Testataan top-listauksen palauttavaa metodia
        """
        pelaaja = self.stats.search("Lemieux")
        pelaaja2 = self.stats.search("Gretzky")
        top_lista = self.stats.top(2)

        self.assertIn(pelaaja, top_lista)
        self.assertIn(pelaaja2, top_lista)
   
