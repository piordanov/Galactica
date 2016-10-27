from abc import ABCMeta


class Ship:
    __metaclass__ = ABCMeta
    # amount of income required to build this ship
    cost = 1

    def __init__(self, player=None):
        self._attack_val = 1
        self._defense_val = 1
        self._maxhp = 1
        self._hp = self._maxhp
        self._player = player

    # @return amount needed on die roll to deal damage while attacker
    @property
    def get_attack(self):
        return self._attack_val

    # @return amount needed on die roll to deal damage while defender
    @property
    def get_defense(self):
        return self._defense_val

    # desc recovers health fully
    # only used by battleship, which has 2 hp instead of 1
    # all other ships are destroyed instantly when damaged
    def heal(self):
        self._hp = self._maxhp

    def __str__(self):
        return "%s at hp %s" % (self.__name__, self._hp)


class StrikeCraft(Ship):
    cost = 3

    def __init__(self):
        Ship.__init__(self)
        self._attack_val = 1
        self._defense_val = 2


class Cruiser(Ship):
    cost = 10

    def __init__(self):
        Ship.__init__(self)
        self._attack_val = 3
        self._defense_val = 2


class BattleShip(Ship):
    cost = 16

    def __init__(self):
        Ship.__init__(self)
        self._attack_val = 4
        self._defense_val = 4
        self._maxhp = 2
        self._hp = self._maxhp


class Destroyer(Ship):
    cost = 8

    def __init__(self):
        Ship.__init__(self)
        self._attack_val = 2
        self._defense_val = 3
