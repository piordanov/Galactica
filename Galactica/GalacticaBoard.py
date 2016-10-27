import Player


class Board:

    def __init__(self, num_players=2, players=None):
        self.graph = []
        self.players = []
        if players is not None:
            self.players = players
        else:
            colors = ['red', 'blue', 'yellow', 'green', 'cyan', 'purple', 'orange', 'pink']
            for i in range(0, num_players):
                self.players.append(Player.Player(colors[i]))

    def add_planet(self, planet):
        self.graph.append(planet)

    @staticmethod
    def add_connection(planet1, planet2):
        planet1.add_neighbor(planet2)
        planet2.add_neighbor(planet1)


class Planet:
    # Planet represented as Vertex in graph

    def __init__(self, name, income):
        self._name = name
        self._income = income
        self._fleet = []
        self._neighbors = []

    def add_neighbor(self, planet):
        self._fleet.append(planet.name)

    def send_in_fleet(self, fleetships):
        for ship in fleetships:
            self._fleet.append(ship)

    def remove_fleet(self, fleetships):
        for ship in fleetships:
            if ship not in self._fleet:
                raise Exception('removing ship not in fleet', self._name, ship.__class__)
            else:
                self._fleet.remove(ship)


    @property
    def get_income(self):
        return self._income

