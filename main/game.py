import random
from data_Handling import save


# Lists of information
locations = ['menu', 'explore']
active_Enemy_List = []
enemy_Attributes = {'Goblin': ['Goblin', 100, 5, 10],
                    'Ogre': ['Ogre', 100, 5, 0]
                    }


# Class for player
class Avatar:
    def __init__(self, Name, Hp, Exp, Str, Mp, location):
        self.__Name = Name
        self.__Hp = Hp
        self.__Exp = Exp
        self.__Str = Str
        self.__Mp = Mp
        self.__Location = location

    # Getter methods
    def get_Name(self):
        return self.__Name

    def get_Hp(self):
        return self.__Hp

    def get_Exp(self):
        return self.__Exp

    def get_Str(self):
        return self.__Str

    def get_Mp(self):
        return self.__Mp

    def get_Location(self):
        return self.__Location

    # Setter methods
    def set_Name(self, newName):
        self.__Name = newName

    def set_Hp(self, newHp):
        self.__Hp = newHp

    def set_Exp(self, newExp):
        self.__Exp = newExp

    def set_Str(self, newStr):
        self.__Str = newStr

    def set_Mp(self, newMP):
        self.__Mp = newMP

    def set_Location(self, location):
        self.__Location = location

    # Might make exploring its own class, not sure yet
    def explore(self, location):
        if location.lower() in locations:
            self.set_Location(location)
        else:
            print('Invalid Location')


# class for enemy NPCs
class Enemy:
    def __init__(self, Name, Hp, Str, Mp):
        self.__name = Name
        self.__hp = Hp
        self.__Str = Str
        self.__Mp = Mp

    def set_Name(self, name):
        self.__name = name

    def set_Hp(self, hp):
        self.__hp = hp

    def set_Str(self, Str):
        self.__Str = Str

    def set_Mp(self, mp):
        self.__Mp = mp

    def get_Name(self):
        return self.__name

    def get_Hp(self):
        return self.__hp

    def get_Str(self):
        return self.__Str

    def get_Mp(self):
        return self.__Mp

    @staticmethod
    def rand_Enemy():
        global active_Enemy_List
        enemy = random.choice(list(enemy_Attributes.keys()))
        name, Hp, Str, Mp = enemy_Attributes[enemy]
        enemy = Enemy(name, Hp, Str, Mp)
        active_Enemy_List.append(enemy)
        return enemy

    # Broken ATM
    # @staticmethod
    # def kill(enemy):
    #     active_Enemy_List.pop(enemy)


# Class for combat/fighting
class Combat:

    @staticmethod
    def initiation(player):
        # Player Stats
        player_Goes_First = False

        # Enemy Stats
        enemy = Enemy.rand_Enemy()
        enemy_Goes_First = False

        # Test
        print("Player is ", player.get_Name())
        print("Enemy is ", enemy.get_Name())

        battle_Active = True

        # Check who attacks first
        # Will change to speed when speed is implemented
        if player.get_Mp() > enemy.get_Mp():
            player_Goes_First = True
        elif player.get_Mp() > enemy.get_Mp():
            enemy_Goes_First = True

        # Where the magic happens
        while battle_Active:
            if player.get_Hp() > 0:
                if player_Goes_First:
                    damage = player.get_Str()
                    enemy_Health = enemy.get_Hp()
                    enemy_Health -= damage
                    print("Player attacked")
                    enemy.set_Hp(enemy_Health)

                    # make condition to check if enemy is dead before attacking player
                    if enemy.get_Hp() > 0:
                        damage = enemy.get_Str()
                        player_Health = player.get_Hp()
                        player_Health -= damage
                        print("Enemy attacked")
                        player.set_Hp(player_Health)
                    else:
                        print("Enemy has 0 or less health")
                elif enemy_Goes_First:
                    if enemy.get_Hp() > 0:
                        damage = enemy.get_Str()
                        player_Health = player.get_Hp()
                        player_Health -= damage
                        print("Enemy attacked")
                        player.set_Hp(player_Health)

                        if player.get_Hp > 0:
                            damage = player.get_Str()
                            enemy_Health = enemy.get_Hp()
                            enemy_Health -= damage
                            print("Player attacked")
                            enemy.set_Hp(enemy_Health)
                        else:
                            print("Player has 0 or less health")
            else:
                print("Player has 0 or less health")

            # Check if player is dead
            if player.get_Hp() <= 0 or enemy.get_Hp() <= 0:
                print("Battle over, set battle_Active False")
                battle_Active = False
        else:
            # Do this if player is dead
            if player.get_Hp() <= 0:
                # add death screen eventually
                print("Player lost all health...")
                exit()
            # Do this if player wins
            elif enemy.get_Hp() <= 0:
                # Enemy.kill(enemy)
                print("Enemy lost all health...")
                print("Giving award to player")
                Combat.reward_System(player)

    # Reward system if player wins
    @staticmethod
    def reward_System(player):
        exp = player.get_Exp()
        exp += 10
        player.set_Exp(exp)


# Create a character
def create_Character(Name, Hp, Exp, Str, Mp, location):
    player = Avatar(Name, Hp, Exp, Str, Mp, location)
    save(player)

    # def character_Callback(self):
    #     tkinter.messagebox.showinfo('Character', 'Name: ' + self.__player.get_Name()
    #                                 + '\nHP: ' + str(self.__player.get_Hp())
    #                                 + '\nEXP: ' + str(self.__player.get_Exp())
    #                                 + '\nStr: ' + str(self.__player.get_Str())
    #                                 + '\nMP: ' + str(self.__player.get_Mp())
    #                                 + '\nLocation: ' + self.__player.get_Location())
