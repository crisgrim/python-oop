class Player():
    # Properties
    name = ''
    age = 0
    role = ''

    # Constructor
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role


class Team():
    players = []

    def show_team(self):
        for player in self.players:
            print(player.name, player.age, player.role)

    def add_player(self, player):
        self.players.append(player)


player1 = Player('Cristina', 18, 'defense')
player2 = Player('Adrián', 18, 'attach')

team1 = Team()
team1.add_player(player1)
team1.add_player(player2)

team1.show_team()
