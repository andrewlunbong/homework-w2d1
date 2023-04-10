class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach

    def add_player(self, input_new_player):
        self.players.append(input_new_player)

    def has_player(self, has_player):
        return has_player in self.players



