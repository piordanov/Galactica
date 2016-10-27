class Board:

    def __init__(self):
        self.graph = []

    def addplanet(self, planet):
        self.graph.add(planet)

    def add_connection(self,planet1,planet2):
        planet1.add_neighbor(planet2)
        planet2.add_neighbor(planet1)


class Planet:
    # Planet represented as Vertex in graph

    def __init__(self, name, income):
        self._name = name
        self._income = income
        self._fleet = []
        self._neighbors = []

    def send_fleet(self, fleetships):
        for ship in fleetships:
            self._fleet.append(ship)

    def add_neighbor(self, planet):
        self._fleet.append(planet.name)

    @property
    def get_income(self):
        return self._income

