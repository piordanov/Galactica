import unittest
from Galactica import Planet, Ship


class ShipTest(unittest.TestCase):
    def setUp(self):
        self.planet1 = Planet.Planet('test1', 3)
        self.planet2 = Planet.Planet('test2', 4)

    def test_init(self):
        self.assertEqual(self.planet1.get_income(), 3)

    def test_neighbors(self):
        self.planet1.add_neighbor(self.planet2)
        self.assertTrue("test2" in self.planet1.get_neighbors())

    def test_add_remove_fleet(self):
        ships = [Ship.Destroyer(), Ship.BattleShip(), Ship.Cruiser(), Ship.StrikeCraft()]
        self.planet1.send_in_fleet(ships)
        self.assertEqual(len(self.planet1.get_fleet()), 4)

        self.planet1.remove_fleet(ships)
        self.assertEqual(len(self.planet1.get_fleet()), 0)

