import random
from tkinter import Tk, BOTH, StringVar, Label, Entry
from tkinter.ttk import Frame, Button, Style
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


# Main menu GUI
class MenuGui(Frame):
    def __init__(self, player):
        super().__init__()
        self.__player = player

        self.style = Style()

        self.name_Value = StringVar()
        self.exp_Value = StringVar()
        self.hp_Value = StringVar()
        self.str_Value = StringVar()
        self.mp_Value = StringVar()

        self.initUI()

    def get_name_Value(self):
        return self.name_Value

    def get_exp_Value(self):
        return self.exp_Value

    def get_hp_Value(self):
        return self.hp_Value

    def get_str_Value(self):
        return self.str_Value

    def get_mp_Value(self):
        return self.mp_Value

    def set_Name_Value(self):
        self.name_Value = str(self.__player.get_Name())

    def set_exp_Value(self):
        self.exp_Value = str(self.__player.get_Exp())

    def set_hp_Value(self):
        self.hp_Value = str(self.__player.get_Hp())

    def set_str_Value(self):
        self.str_Value = str(self.__player.get_Str())

    def set_mp_Value(self):
        self.mp_Value = str(self.__player.get_Mp())

    def set_All_Values(self):
        self.name_Value = str(self.__player.get_Name())
        self.exp_Value = str(self.__player.get_Exp())
        self.hp_Value = str(self.__player.get_Hp())
        self.str_Value = str(self.__player.get_Str())
        self.mp_Value = str(self.__player.get_Mp())

    def get_All_Values(self):
        # Throwing error: "AttributeError: 'str' object has no attribute 'set' WHY?
        try:
            self.name_Value.set(self.get_name_Value())
            self.exp_Value.set(self.get_exp_Value())
            self.hp_Value.set(self.get_hp_Value())
            self.str_Value.set(self.get_str_Value())
            self.mp_Value.set(self.get_mp_Value())
        except AttributeError:
            print("ATTRIBUTE ERROR 'str' object has no attribute 'set'")
            exit()

    def initUI(self):
        self.style.theme_use("default")

        self.master.title("Test")
        self.pack(fill=BOTH, expand=1)

        stats_Label = Label(self, text="Stats:")
        stats_Label.place(x=80, y=10)

        name_Label = Label(self, text='Name: ')
        name_Label.place(x=90, y=30)
        name_Value_Label = Label(self, textvariable=self.hp_Value)
        name_Value_Label.place(x=140, y=30)

        exp_Label = Label(self, text='EXP: ')
        exp_Label.place(x=90, y=50)
        exp_Value_Label = Label(self, textvariable=self.exp_Value)
        exp_Value_Label.place(x=140, y=50)

        hp_Label = Label(self, text="HP : ")
        hp_Label.place(x=90, y=70)
        hp_Value_Label = Label(self, textvariable=self.hp_Value)
        hp_Value_Label.place(x=140, y=70)

        str_Label = Label(self, text="STR: ")
        str_Label.place(x=90, y=90)
        str_Value_Label = Label(self, textvariable=self.str_Value)
        str_Value_Label.place(x=140, y=90)

        mp_Label = Label(self, text="MP: ")
        mp_Label.place(x=90, y=110)
        mp_Value_Label = Label(self, textvariable=self.mp_Value)
        mp_Value_Label.place(x=140, y=110)

        explore_Button = Button(self, text="Explore", command=self.explore_Callback)
        explore_Button.place(x=10, y=10)

        save_Button = Button(self, text="Save", command=self.save_Callback)
        save_Button.place(x=10, y=50)

        quit_Button = Button(self, text="Quit", command=self.quit_Callback)
        quit_Button.place(x=10, y=90)

    def save_Callback(self):
        save(self.__player)
        self.set_All_Values()
        self.get_All_Values()

    def explore_Callback(self):
        Combat.initiation(self.__player)

    def quit_Callback(self):
        save(self.__player)
        exit()


# Not really needed rn
# Settings Gui
# class SettingsGui:
#     def __init__(self):
#         self.main_Window = tkinter.Tk()
#
#         pass


# Gui to create character if not found in save file
class CharacterCreationGui:
    def __init__(self):
        self.main_Window = Tk()

        self.top_Frame = Frame(self.main_Window)
        self.mid_Frame = Frame(self.main_Window)
        self.bottom_Frame = Frame(self.main_Window)

        self.label_1 = Label(self.top_Frame, text='Hello! Welcome to my game. This is a test.')

        self.label_1.pack(side='top')

        self.label_2 = Label(self.mid_Frame, text='Name: ')
        self.entry_1 = Entry(self.mid_Frame, width=10)

        self.label_2.pack(side='left')
        self.entry_1.pack(side='left')

        self.button_1 = Button(self.bottom_Frame, text='Create', command=self.create_Callback)

        self.button_1.pack(side='top')

        self.top_Frame.pack()
        self.mid_Frame.pack()
        self.bottom_Frame.pack()

        root = Tk()

        root.mainloop()

    def create_Callback(self):
        Name = self.entry_1.get()
        create_Character(Name, 10, 0, 10, 10, 'start')
        self.main_Window.destroy()
