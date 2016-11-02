class Player:

    def __init__(self, color="white"):
        self._planets = set()
        self._color = color

    def assign_planet(self,planet):
        self._planets.add(planet)

    def get_planets(self):
        return self._planets

    def get_color(self):
        return self._color

    def __str__(self):
        result = self._color + ":"
        for planet in self._planets:
            result += " " + planet.get_name()
        return result
