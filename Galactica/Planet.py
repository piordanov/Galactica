class Planet:
    # Planet represented as Vertex in graph

    def __init__(self, name, income=1):
        self._name = name
        self._income = income
        self._fleet = []
        self._neighbors = set()
        self._factory = False

    def add_neighbor(self, planet):
        self._neighbors.add(planet.get_name())

    def send_in_fleet(self, fleetships):
        for ship in fleetships:
            self._fleet.append(ship)

    def remove_fleet(self, fleetships):
        for ship in fleetships:
            if ship not in self._fleet:
                raise Exception('removing ship not in fleet', self._name, ship.__class__)
            else:
                self._fleet.remove(ship)

    def increase_income(self):
        self._income += 1

    def add_factory(self):
        self._factory = True

    def has_factory(self):
        return self._factory

    def get_income(self):
        return self._income

    def get_fleet(self):
        return self._fleet

    def get_neighbors(self):
        return self._neighbors

    def get_name(self):
        return self._name

    def __str__(self):
        return "Planet: " + self._name + " Income: " + str(self._income)
