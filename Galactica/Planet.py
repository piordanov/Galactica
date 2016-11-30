class Planet:
    # Planet represented as Vertex in graph

    def __init__(self, name, income=1):
        self._name = name
        self._income = income
        self._fleet = {}
        self._neighbors = set()
        self._factory = False

    def add_neighbor(self, planet):
        self._neighbors.add(planet.get_name())

    def send_in_fleet(self, fleetships, player):
        if player not in self._fleet:
            self._fleet[player] = []
        for ship in fleetships:
            self._fleet[player].append(ship)

    def remove_fleet(self, ship_names, player):
        temp = []
        if player not in self._fleet:
            return []
        fleet = self._fleet[player]
        for name in ship_names:
            ship = [item for item in fleet if item.get_name() == name]
            if ship not in fleet:
                for temp_ship in temp:
                    fleet.append(temp_ship)
                return []
                # raise Exception('removing ship not in fleet', self._name, ship.__class__)
            else:
                fleet.remove(ship)
                temp.append(ship)
        return temp

    def is_contested(self):
        found_fleet = False
        for fleet in self._fleet.values():
            if len(fleet) > 0 and not found_fleet:
                found_fleet = True
            elif len(fleet) > 0 and found_fleet:
                return True
        return False

    def get_contestors(self):
        result = []
        for player, fleet in self._fleet.iteritems():
            if len(fleet) > 0:
                result.append(player)
        return result

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

    def get_player_fleet(self, playername):
        if playername in self._fleet:
            return self._fleet[playername]
        return None

    def get_neighbors(self):
        return self._neighbors

    def get_name(self):
        return self._name

    def __str__(self):
        result = "Planet: " + self._name + " Income: " + str(self._income)
        result += '\nNeighbors:\n'
        result += ', '.join(map(str, self.get_neighbors())) # http://stackoverflow.com/questions/2399112/python-print-delimited-list
        result +='\nShips in orbit:\n'
        # result += ', '.join(map(str, self.get_fleet()))
        for player, fleet in self._fleet.iteritems():
            result += str(player) + ' : ' + str(fleet) + '\n'
        return result

    @staticmethod
    # @desc selects the ships corresponding with names in fleet from planet1 to planet2
    # @param src_planet_name where the fleet originates from if a ship designated in fleet doesn't exist,
    #   this functions changes nothing and returns 1
    # @param dest_planet_name where the fleet will end up after the function returns
    # @param fleet string array of ship names expected to be in src_planet
    # @return True for successful transfer of ships in fleet from source to destination False otherwise
    def move_fleet(src_planet, dest_planet, fleet, player):
        if not fleet:
            return False

        fleet_ships = src_planet.remove_fleet(fleet, player)
        if not fleet_ships:
            return False
        dest_planet.send_in_fleet(fleet_ships, player)
        return True
