import unittest
from Galactica import Ship


class ShipTest(unittest.TestCase):
    def test_init(self):
        ship = Ship.StrikeCraft()
        self.assertEqual(ship.get_attack, 1)
        ship = Ship.Cruiser()
        self.assertEqual(ship.get_attack, 3)
        ship = Ship.Destroyer()
        self.assertEqual(ship.get_attack, 2)
        ship = Ship.BattleShip()
        self.assertEqual(ship.get_attack, 4)

