import unittest
import random
from Galactica import GalacticaBoard, Planet


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = GalacticaBoard.Board()

    def test_generate_world(self):
        self.board._graph = []
        for i in range(0, 4):
            planet = Planet.Planet('test' + str(i), random.randint(0, 5))
            self.board.add_planet(planet)

        GalacticaBoard.add_connection(self.board._graph[0], self.board._graph[1])
        GalacticaBoard.add_connection(self.board._graph[0], self.board._graph[2])
        GalacticaBoard.add_connection(self.board._graph[1], self.board._graph[3])

        self.board.print_board()

    def test_random_name_gen(self):
        print "test random names\n"
        print GalacticaBoard.Board.get_random_planet_names(3)

    def test_random_world(self):
        print "test random world\n"
        self.board.generate_random_universe(10, 0.2, 6)
        self.board.print_board()

    def test_get_planet(self):
        test_planet = Planet.Planet('testworld')
        self.board.add_planet(test_planet)
        self.assertEqual(test_planet.get_income(), self.board.get_planet('testworld').get_income())

