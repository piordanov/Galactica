import GalacticaBoard
import Ship
import Planet
import Player


#pygame UI for galactica
class Galactica:

    def __init__(self):
        self.board = None
        self.curr_player = 0


    def start_game_loop(self):
        print "Welcome to Galactica, press D to start debug mode or Q to quit"
        done = False
        while not done:
            result = raw_input("Main Menu>")
            if result == 'Q':
                done = True
            elif result == 'D':
                self.debug_mode()
        print "Good Bye"

    def debug_mode(self):
        notdone = True
        curr_player_idx = 0
        print "Generating Debug World"
        self.board = GalacticaBoard.Board()
        print "Success"
        self.print_help()

        while notdone:
            self.next_player()
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
        print 'Q : quits'


    def parse_command(self, command):
        if command == 'player':
            player = self.get_curr_player()
            print player
            return True
        if command == "H":
            self.print_help()
            return True
        if command == 'print board':
            print "Printing Board"
            self.board.print_board()
            return True
        commands = command.split(' ', 1)
        if commands[0] == 'details':
            if len(commands) > 1:
                planet_name = commands[1]
                print str(self.board.get_planet(planet_name))
                return True
            else:
                return False

        return False

    def get_curr_player(self):
        return self.board.get_players()[self.curr_player]

    def next_player(self):
        self.curr_player += 1
        if self.curr_player >= len(self.board.get_players()):
            self.curr_player = 0

if __name__ == "__main__":
    g = Galactica()
    g.start_game_loop()