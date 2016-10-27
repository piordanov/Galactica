import GalacticaBoard
import Player


class Galactica:

    def __init__(self, num_players=2):
        self.board = GalacticaBoard.Board()
        self.players = []
        colors = ['red', 'blue', 'yellow', 'green', 'cyan', 'purple', 'orange', 'pink']
        for i in range(0,num_players):
            self.players.append(Player.Player(colors[i]))



