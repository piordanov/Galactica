import unittest
from Galactica import Player, Planet


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player.Player()
        planet1 = Planet.Planet('test1', 1)
        planet1.add_factory()
        planet2 = Planet.Planet('test2', 1)

        self.player.assign_planet(planet1)
        self.player.assign_planet(planet2)

    def test_collect_income(self):
        self.player.collect_income()
        self.assertTrue(self.player.curr_income == 22)

    def test_purchase_fleet(self):

        self.assertTrue(self.player.owns_planet('test1'))
        self.player.add_income(37) # cost to buy these ships
        fleet = ['Destroyer', 'BattleShip', 'Cruiser', 'StrikeCraft']

        planet = self.player.get_planet('test1')
        self.player.buy_fleets(fleet, planet)

        self.assertEqual(len(planet.get_fleet()), 4)
        self.assertEqual(20, self.player.get_income())
