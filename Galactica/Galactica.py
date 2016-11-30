import GalacticaBoard
import Ship
import Planet
import Player
import shlex
import random
from enum import Enum


Phase = Enum('Phase', 'buy move fight place')

class Galactica:

    def __init__(self):
        self.board = None
        self.curr_player = 0
        self.curr_phase = Phase.buy
        self.purchase_list = []
        self.temp_income = 0
        self.contested_planets = set()


    def main_menu_loop(self):
        print "Welcome to Galactica, press D to start debug mode or Q to quit"
        done = False
        while not done:
            result = raw_input("Main Menu>")
            if result == 'Q':
                done = True
            elif result == 'D':
                self.debug_mode()
            elif result == 'S':
                self.board = GalacticaBoard.Board()
                self.temp_income = self.get_curr_player().get_income()
                self.start_game_loop()

        print "Good Bye"

    def debug_mode(self):
        notdone = True
        curr_player_idx = 0
        print "Generating Debug World"
        self.board = GalacticaBoard.Board()
        self.temp_income = self.get_curr_player().get_income()
        print "Success"
        self.print_help()

        self.start_game_loop()

    def start_game_loop(self):
        notdone = True
        while notdone:
            command = raw_input("> ")
            if command == "Q":
                notdone = False
                continue
            if not self.parse_command(command):
                print "Invalid command"
                self.print_help()

    def print_help(self):
        print "H : reveals this help menu"
        print "player : prints current player"
        print "details <planet_name> : prints details of planet"
        print 'print board : prints entire board'
        print 'owned planets : prints planets owned by the player'
        print 'phase : return the current phase'
        print 'income : return the player\'s current income'
        print 'buy <ship_name> <num>: purchase a ship only if in buy phase if no num given, defaults to 1'
        print 'move <ship_name> \'<planet1>\' \'<planet2>\' <num> : move num ships from planet1 to planet2 ' \
            'if no num given, defaults to 1 only if in move phase'
        print 'place <ship_name> <planet> : spawn a ship from purchased at planet '
        print 'Q : quits game'

    def parse_command(self, command):
        if command == 'player':
            self.print_curr_player()
        elif command == "H":
            self.print_help()
        elif command == 'print board':
            print "Printing Board"
            self.board.print_board()
        elif command == 'owned planets':
            print 'Controlled Planets'
            self.print_owners_planets()
        elif command == 'income':
            print "Income: " + str(self.get_curr_player().get_income())
        elif command == 'phase':
            self.print_curr_phase()
        elif command == 'next':
            self.next_phase()
            self.print_curr_phase()
        else:
            commands = command.split(' ', 1)
            if commands[0] == 'details' and len(commands) == 2:
                planet_name = commands[1]
                self.get_details_of_planet(planet_name)
                return True
                # http://stackoverflow.com/questions/79968/split-a-string-by-spaces-preserving-quoted-substrings-in-python
            commands = shlex.split(command)
            if commands[0] == 'buy' and self.curr_phase == Phase.buy and len(commands) > 1:
                num = 1
                if len(commands) == 3:
                    num = int(commands[2])
                self.purchase_ship(commands[1], num)

            elif commands[0] == 'move' and self.curr_phase == Phase.move and len(commands) > 2:
                num_ships = 1
                if len(commands) > 3:
                    num_ships = commands[4]
                planet1 = self.board.get_planet(commands[2])
                planet2 = self.board.get_planet(commands[3])
                ships = [commands[1]] * num_ships
                Planet.Planet.move_fleet(planet1, planet2, ships, self.get_curr_player().get_name())
                if planet2.is_contested():
                    self.contested_planets.add(planet2)
                elif not self.get_curr_player().owns_planet(planet2):
                    self.get_curr_player().assign_planet(planet2)

            elif commands[0] == 'place' and self.curr_phase == Phase.place and len(commands) > 2:
                will_place = False
                for i, ship in enumerate(self.purchase_list):
                    if ship.get_name() == commands[1]:
                        self.purchase_list.pop(i)
                        will_place = True
                        break
                planet = self.board.get_planet(commands[2])
                if planet is not None and self.get_curr_player().buy_fleets([commands[1]], planet):
                    print commands[1] + " now at " + str(planet)

                else:
                    print "Could not place ship at planet: make sure you have a factory at desired planet"

            else:
                return False

        return True

    # @desc resolves all battles with curr_player as the attacker
    # @param attacker Player that is recognized as attacker, which should be the current player
    # @param contested_planets each planet with the attacker having a fleet inside alongside another fleet
    #   and not owned by the attacker
    def resolve_all_battles(self, attacker, contested_planets):
        for planet in contested_planets:
            other_players = planet.get_contesters()
            defender_name = other_players.remove(attacker.get_name())[0]
            defender = self.board.get_player(defender_name)
            self.resolve_battle(attacker, defender, planet)

    def resolve_battle(self, attacker, defender, planet):
        attacker_fleet = planet.get_player_fleet(attacker.get_name())
        defender_fleet = planet.get_player_fleet(defender.get_name())

        while not attacker_fleet or not defender_fleet:
            print "Attackers:"
            print attacker_fleet
            print "Defenders:"
            print defender_fleet

            print "Hits distributed by attackers:"
            attacker_hits = Galactica.roll_hits(attacker_fleet, True)
            print "Hits distributed by defenders:"
            defender_hits = Galactica.roll_hits(defender_fleet, False)

            for i in range(0, defender_hits):
                if attacker_fleet:
                    attacker_fleet.pop()
            for i in range(0, attacker_hits):
                if defender_fleet:
                    defender_fleet.pop()

        if attacker_fleet and not defender_fleet:
            attacker.assign_planet(planet)
            defender.lose_planet(planet)





    @staticmethod
    def roll_hits(fleet, attacking):
        result = 0
        for ship in fleet:
            die = random.randint(1, 6)
            if attacking and die <= ship.get_attack():
                result += 1
            if not attacking and die <= ship.get_defense():
                result += 1
        return result

    def get_details_of_planet(self, planet_name):
        planet = self.board.get_planet(planet_name)
        if planet is None:
            print "Planet " + planet_name + " not found"
        elif self.board.get_owner(planet):
            print "Owned by: " + self.board.get_owner(planet).get_name()
        print str(planet)

    def purchase_ship(self, ship_name, num):
        ships = [Ship.gen_ship(ship_name) for i in range(num)]
        if None in ships:
            return
        cost = sum(ship.cost for ship in ships)
        if self.temp_income >= cost:
            self.temp_income -= cost
            self.purchase_list.extend(ships)
            print "Purchasing " + str(num) + " of " + ship_name
            print "Income left: " + str(self.temp_income)

    def next_phase(self):
        if self.curr_phase == Phase.place:
            if len(self.purchase_list) > 0:
                print "Still have not placed all ships."
                return
            self.get_curr_player().collect_income()
            self.next_player()
            self.set_phase(Phase.buy)
            self.temp_income = self.get_curr_player().get_income()
            self.purchase_list = []
            self.print_curr_player()
        elif self.curr_phase == Phase.buy:
            self.set_phase(Phase.move)
        elif self.curr_phase == Phase.move:
            self.set_phase(Phase.fight)
            self.resolve_all_battles(self.get_curr_player(), self.contested_planets)
            self.contested_planets = set()
            self.set_phase(Phase.place)

    def set_phase(self, phase):
        self.curr_phase = phase

    def print_curr_phase(self):
        print self.curr_phase.name + " Phase"

    def get_curr_player(self):
        return self.board.get_players()[self.curr_player]

    def print_curr_player(self):
        print 'Player ' + str(self.get_curr_player().get_name()) + ' it is now your turn'

    def print_owners_planets(self):
        for planet in self.get_curr_player().get_planets():
            print str(planet)

    def next_player(self):
        self.curr_player += 1
        if self.curr_player >= len(self.board.get_players()):
            self.curr_player = 0

if __name__ == "__main__":
    g = Galactica()
    g.main_menu_loop()