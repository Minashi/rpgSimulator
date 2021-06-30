import random
import pickle

active_Enemy_List = []
enemy_Attributes = {'Goblin': ['Goblin', 100, 0, 10, 10],
                    'Ogre': ['Ogre', 200, 0, 50, 0]
                    }


class Avatar:
    def __init__(self, Name, Hp, Exp, Str, Mp):
        self.__Name = Name
        self.__Hp = Hp
        self.__Exp = Exp
        self.__Str = Str
        self.__Mp = Mp

    def get_name(self):
        return self.__Name

    def get_Hp(self):
        return self.__Hp

    def get_Exp(self):
        return self.__Exp

    def get_Str(self):
        return self.__Str

    def get_Mp(self):
        return self.__Mp

    def set_name(self, newName):
        self.__Name = newName

    def set_Hp(self, newHp):
        self.__Hp = newHp

    def set_Exp(self, newExp):
        self.__Exp = newExp

    def set_Str(self, newStr):
        self.__Str = newStr

    def set_Mp(self, newMP):
        self.__Mp = newMP

    # def __str__(self):
    #     return self.__Name + self.__Hp + self.__Exp + self.__Str + self.__Mp


class Enemy(Avatar):
    def __init__(self, Name, Hp, Exp, Str, Mp):
        super().__init__(Name, Hp, Exp, Str, Mp)

    @staticmethod
    def rand_Enemy():
        global active_Enemy_List
        enemy = random.choice(list(enemy_Attributes.keys()))
        name, Hp, Exp, Str, Mp = enemy_Attributes[enemy]
        enemy = Enemy(name, Hp, Exp, Str, Mp)
        active_Enemy_List.append(enemy)
        return enemy

    @staticmethod
    def kill(enemy):
        active_Enemy_List.pop(enemy)

    # def __str__(self):
    #     return self.__Name + self.__Hp + self.__Exp + self.__Str + self.__Mp


class Travel(Avatar):
    def __init__(self, Name, Hp, Exp, Str, Mp, Location):
        super().__init__(Name, Hp, Exp, Str, Mp)
        self.__Location = Location


class Combat:

    @staticmethod
    def initiation(player, npc):
        print("Player is ", player.get_name())
        print("Enemy is ", npc.get_name())


def create_Character(Name, Hp, Exp, Str, Mp):
    player = Avatar(Name, Hp, Exp, Str, Mp)
    save(player)


def save(plyr):
    FILE_NAME = 'saveFile.txt'
    again = True
    output_file = open(FILE_NAME, 'wb')

    while again:
        pickle.dump(plyr, output_file)
        again = False

    output_file.close()
    print("Data was written to ", FILE_NAME)


def load():
    FILE_NAME = 'saveFile.txt'
    end_of_file = False
    input_file = open(FILE_NAME, 'rb')

    while not end_of_file:
        try:
            player_Save = pickle.load(input_file)
        except EOFError:
            end_of_file = True

    input_file.close()
    return player_Save