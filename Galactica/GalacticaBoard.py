import Player
import Planet
import random


def add_connection(planet1, planet2):
    planet1.add_neighbor(planet2)
    planet2.add_neighbor(planet1)


class Board:

    def __init__(self, players=None, num_players=2, num_planets=8, prob=0.2, income_range=6):
        self._graph = []
        self._players = []
        if players is not None:
            self._players = players
        else:
            self.generate_players(num_players)
        self.generate_random_universe(num_planets, prob, income_range)
        self.assign_player_homeworlds()

    # creates num_players players with random colors
    # @param num_players number of players available on the board
    # @return nothing changes the state of the board
    def generate_players(self, num_players):
        colors = ['red', 'blue', 'yellow', 'green', 'cyan', 'purple', 'orange', 'pink']
        for i in range(0, num_players):
            self._players.append(Player.Player(colors[i], colors[i]))

    # desc creates a new world based of this explanation
    # http://stackoverflow.com/questions/20171901/how-to-generate-random-graphs
    # @param num_planets number of nodes in graph
    # @param prob defines the density of the world
    # @param income_range max amount of income a planet can have
    # @return nothing changes the state of the board
    def generate_random_universe(self, num_planets, prob, income_range):
        planet_names = self.get_random_planet_names(num_planets)
        for i in range(0,num_planets):
            income = random.randint(1, income_range)
            planet_name = planet_names[i]
            planet = Planet.Planet(planet_name, income)
            self.add_planet(planet)

        for idx, planet in enumerate(self._graph):
            # stackoverflow.com/questions/2142453/getting-list-without-kth-element-efficiently-and-non-destructively
            neighbors = [elt for num, elt in enumerate(self._graph) if not num == idx]
            for neighbor in neighbors:
                # connect nodes with probability prob
                chance = random.uniform(0, 1)
                if chance < prob:
                    add_connection(planet, neighbor)

        # @TODO ensure that graph is connected

    def assign_player_homeworlds(self):
        rand_planets = random.sample(self._graph,len(self._players))
        for i, player in enumerate(self._players):
            random_planet = rand_planets[i]
            player.assign_planet(random_planet)
            random_planet.add_factory()

    def add_planet(self, planet):
        self._graph.append(planet)

    def get_planet(self, planet_name):
        planets_with_name = [item for item in self._graph if item.get_name() == planet_name]
        if planets_with_name:
            return planets_with_name[0]
        return None

    def get_all_planets(self):
        return self._graph

    # @desc returns the player who owns the planet with the given name
    # @param planet_name string of the planet's name
    # @return Player who owns planet with name planet_name, or None if no player owns given planet, if one exists
    def get_owner(self, planet_name):
        for player in self._players:
            if player.owns_planet(planet_name):
                return player
        return None

    def get_players(self):
        return self._players

    def get_player(self, playername):
        return [item for item in self._players if item.get_name() == playername][0]

    # @desc picks words from our source of random planet names acquired from fantasynamegenerators.com/planet_names.php
    # @param n the number of planet names required
    # @return a list of random planet names
    @staticmethod
    def get_random_planet_names(n):
        with open('./resources/planetnames.txt') as f:
            content = f.readlines()
        random.shuffle(content)
        result = content[0:n]
        return [s.rstrip() for s in result]

    # @desc prints to console string representation of board
    # @return nothing
    def print_board(self):
        for planet in self._graph:
            print str(planet)

        for player in self._players:
            print str(player)


