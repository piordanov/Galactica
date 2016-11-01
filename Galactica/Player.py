class Player:

    def __init__(self, color="white"):
        self._planets = []
        self._color = color

    def get_planets(self):
        return self._planets

    def get_color(self):
        return self._color
