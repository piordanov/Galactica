import Ship


class Player:

    def __init__(self, color="white"):
        self._planets = set()
        self._color = color
        self.curr_income = 20

    def owns_planet(self, planet_name):
        return len([item for item in self._planets if item.get_name() == planet_name]) == 1

    def get_planet(self, planet_name):
        return [item for item in self._planets if item.get_name() == planet_name][0]

    def assign_planet(self, planet):
        self._planets.add(planet)

    def add_income(self, amount):
        self.curr_income += amount

    def get_income(self):
        return self.curr_income

    def collect_income(self):
        total_income = 0
        for planet in self.get_planets():
            total_income += planet.get_income()
        self.add_income(total_income)

    # @desc purchases ships and places them at allowed planets
    # @param player Player to buy fleet
    # @param fleet_map which ships to buy
    # @param planet Planet for hte fleet to be placed on
    # @param False if unsuccessful True otherwise
    def buy_fleets(self, fleet_names, planet):
        total_cost = 0
        fleet = []
        if not planet.has_factory() or not self.owns_planet(planet.get_name()):
            return False

        for ship_name in fleet_names:
            ship = Ship.gen_ship(ship_name)
            if ship is not None:
                total_cost += ship.cost
                fleet.append(ship)
            else:
                return False
        purchased = self.remove_income(total_cost)
        if purchased:
            planet.send_in_fleet(fleet)
            return True
        else:
            return False

    # @desc removes amount from income if possible
    # @param amount what is to be removed
    def remove_income(self, amount):
        if self.curr_income - amount < 0:
            return False
        else:
            self.curr_income -= amount
            return True

    def get_planets(self):
        return self._planets

    def get_color(self):
        return self._color

    def __str__(self):
        result = self._color + ":"
        for planet in self._planets:
            result += " " + planet.get_name()
        return result
