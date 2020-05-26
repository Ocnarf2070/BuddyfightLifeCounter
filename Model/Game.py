from Model import Player


class Game:
    def __init__(self, life: int = 10):
        self.__init_life = life
        self.__players = [Player("Player 1", life), Player("Player 2", life)]

    def sub_life_player(self, player: int, cant: int):
        self.__players[player].sub_life(cant)

    def add_life_player(self, player: int, cant: int):
        self.__players[player].add_life(cant)

    def restart(self):
        return Game(self.__init_life)

    def get_players(self) -> [Player]:
        return self.__players

    def set_players(self, players: [Player]):
        self.__players = players

    def get_player(self, p: int) -> Player:
        return self.__players[p]

    def set_player(self, p: int, player: Player):
        self.__players[p] = player

    def __str__(self):
        return str(self.__players[0]) + "\n" + str(self.__players[1])


if __name__ == '__main__':
    game = Game()
    game.add_life_player(0, 2)
    game.add_life_player(0, 5)
    game.sub_life_player(0, 1)
    game.add_life_player(1, 2)
    print(game)
