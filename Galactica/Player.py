class Player:

    def __init__(self, color="white"):
        self.planets = []
        self.color = color

    def get_planets(self):
        return self.planets

    def get_color(self):
        return self.color
