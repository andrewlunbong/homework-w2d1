class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.point = 0

    def add_player(self, input_new_player):
        self.players.append(input_new_player)

    def has_player(self, player):
        return self.players.count(player)>0
        #return player in self.players

    def play_game(self, game_won):
        if game_won:
            self.point += 3    



