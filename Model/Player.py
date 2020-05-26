class Player:
    def __init__(self, name, life):
        self.__name = name
        self.__life = life
        self.__record = [str(life)]

    def add_life(self, cant):
        self.__life += cant
        self.__record.append("+{}".format(cant))
        self.__record.append(str(self.__life))

    def sub_life(self, cant):
        if self.__life == 0:
            return False
        dif = self.__life - cant
        if dif < 0:
            dif = 0
        self.__life = dif
        self.__record.append("-{}".format(cant))
        self.__record.append(str(self.__life))
        return True

    def buddy_call(self):
        self.__life += 1
        self.__record.append("BCall")
        self.__record.append(str(self.__life))

    def last_update(self) -> (str, str):
        size = len(self.__record) - 1
        if size <= 1:
            return " \n", self.__record[size] + "\n"
        return self.__record[size - 1] + '\n', self.__record[size] + '\n'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

    def get_record(self):
        return self.__record

    def set_record(self, hist):
        self.__record = hist

    def __str__(self):
        return "Name: " + self.__name + ", " + \
               "Life: " + str(self.__life) + ", " + \
               "History: " + str(self.__record)


if __name__ == '__main__':
    players = [Player("p1", 10), Player("p2", 10)]
    for player in players:
        print(player)
        print(player.last_update()[1])

    players[0].add_life(999)
    print(players[0].last_update())
    players[1].sub_life(1)
    print(players[1].last_update())

    for player in players:
        print(player)
