import random
import pickle
import tkinter
import tkinter.messagebox

# Lists of information
locations = ['menu', 'explore']
active_Enemy_List = []
enemy_Attributes = {'Goblin': ['Goblin', 100, 10, 10],
                    'Ogre': ['Ogre', 200, 50, 0]
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


# class for enemy NPC's
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

    def set_Str(self, str):
        self.__Str = str

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

    @staticmethod
    def kill(enemy):
        active_Enemy_List.pop(enemy)


# Class for combat/fighting
class Combat:
    def initiation(self, player):
        # Player Stats
        player_Name = player.get_Name()
        player_Hp = player.get_Hp()
        player_Str = player.get_Str()
        player_Mp = player.get_Mp()
        player_Goes_First = False

        # Enemy Stats
        enemy = Enemy.rand_Enemy()
        enemy_Name = enemy.get_Name()
        enemy_Hp = enemy.get_Hp()
        enemy_Str = enemy.get_Str()
        enemy_Mp = enemy.get_Mp()
        enemy_Goes_First = False

        # Test
        print("Player is ", player_Name)
        print("Enemy is ", enemy_Name)

        battle_Active = True

        # Check who attacks first
        # Will change to speed when speed is implemented
        if player_Mp > enemy_Mp:
            player_Goes_First = True
        elif enemy_Mp > player_Mp:
            enemy_Goes_First = True

        # Where the magic happens
        while battle_Active:
            if player_Goes_First:
                pass
            elif enemy_Goes_First:
                pass

            # Check if player is dead
            if player_Hp == 0 or player_Hp < 0:
                battle_Active = False
        else:
            # Do this if player is dead
            if player_Hp == 0 or player_Hp < 0:
                pass
            # Do this if player wins
            else:
                self.reward_System(player)

    # Reward system if player wins
    @staticmethod
    def reward_System(player):
        exp = player.get_Exp()
        pass


# Create a character
def create_Character(Name, Hp, Exp, Str, Mp, location):
    player = Avatar(Name, Hp, Exp, Str, Mp, location)
    save(player)


# Save character stats
def save(plyr):
    FILE_NAME = 'saveFile.txt'
    again = True
    output_file = open(FILE_NAME, 'wb')

    while again:
        pickle.dump(plyr, output_file)
        again = False

    output_file.close()
    print("Data was written to ", FILE_NAME)


# Load character stats
def load():
    FILE_NAME = 'saveFile.txt'
    end_of_file = False
    player_Exists = False
    player_Save = None
    input_file = open(FILE_NAME, 'rb')

    while not end_of_file:
        try:
            player_Save = pickle.load(input_file)
            player_Exists = True
        except EOFError:
            end_of_file = True

    input_file.close()
    return player_Save, player_Exists


# Main menu Gui
class MenuGui:
    def __init__(self, player):
        self.__player = player

        self.main_Window = tkinter.Tk()

        self.menu_Frame = tkinter.Frame(self.main_Window)
        self.menu_Frame_Bottom = tkinter.Frame(self.main_Window)

        self.explore_Button = tkinter.Button(self.menu_Frame, text='Explore', command=self.explore_Callback)
        self.character_Button = tkinter.Button(self.menu_Frame, text='Character', command=self.character_Callback)

        self.explore_Button.pack(side='top')
        self.character_Button.pack(side='top')

        self.space_Label = tkinter.Label(self.menu_Frame_Bottom, text='')
        self.save_Button = tkinter.Button(self.menu_Frame_Bottom, text='Save', command=self.save_Callback)
        self.settings_Button = tkinter.Button(self.menu_Frame_Bottom, text='Settings', command=self.settings_Callback)
        self.quit_Button = tkinter.Button(self.menu_Frame_Bottom, text='Quit', command=self.quit_Callback)

        self.space_Label.pack(side='top')
        self.save_Button.pack(side='left')
        self.settings_Button.pack(side='left')
        self.quit_Button.pack(side='left')

        self.menu_Frame.pack()
        self.menu_Frame_Bottom.pack()

        tkinter.mainloop()

    def explore_Callback(self):
        ExploreGui(self.__player)

    def character_Callback(self):
        tkinter.messagebox.showinfo('Character', 'Name: ' + self.__player.get_Name()
                                        + '\nHP: ' + str(self.__player.get_Hp())
                                        + '\nEXP: ' + str(self.__player.get_Exp())
                                        + '\nStr: ' + str(self.__player.get_Str())
                                        + '\nMP: ' + str(self.__player.get_Mp())
                                        + '\nLocation: ' + self.__player.get_Location())

    def save_Callback(self):
        save(self.__player)

    @staticmethod
    def settings_Callback():
        SettingsGui()

    def quit_Callback(self):
        save(self.__player)
        exit()


# Settings Gui
class SettingsGui:
    def __init__(self):
        self.main_Window = tkinter.Tk()

        pass


# Gui to create character if not found in save file
class CharacterCreationGui:
    def __init__(self):
        self.main_Window = tkinter.Tk()

        self.top_Frame = tkinter.Frame(self.main_Window)
        self.mid_Frame = tkinter.Frame(self.main_Window)
        self.bottom_Frame = tkinter.Frame(self.main_Window)

        self.label_1 = tkinter.Label(self.top_Frame, text='Hello! Welcome to my game. This is a test.')

        self.label_1.pack(side='top')

        self.label_2 = tkinter.Label(self.mid_Frame, text='Name: ')
        self.entry_1 = tkinter.Entry(self.mid_Frame, width=10)

        self.label_2.pack(side='left')
        self.entry_1.pack(side='left')

        self.button_1 = tkinter.Button(self.bottom_Frame, text='Create', command=self.create_Callback)

        self.button_1.pack(side='top')

        self.top_Frame.pack()
        self.mid_Frame.pack()
        self.bottom_Frame.pack()

        tkinter.mainloop()

    def create_Callback(self):
        Name = self.entry_1.get()
        create_Character(Name, 10, 0, 10, 10, 'start')
        self.main_Window.destroy()


# The explore/travel Gui
class ExploreGui:
    def __init__(self, player):
        self.__player = player

        self.main_Window = tkinter.Tk()

        self.button_1 = tkinter.Button(self.main_Window, text='Explore', command=self.explore_Callback)
        self.button_2 = tkinter.Button(self.main_Window, text='return', command=self.return_Callback)

        self.button_1.pack(side='top')
        self.button_2.pack(side='top')

        tkinter.mainloop()

    def explore_Callback(self):
        # add chances to either get loot, or get into a fight. for now I will just make it only combat occurance
        FightGui(self.__player)

    def return_Callback(self):
        self.main_Window.destroy()


# Fight Gui
class FightGui:
    def __init__(self, player):
        self.__player = player
        self.main_Window = tkinter.Tk()

        self.top_Frame = tkinter.Frame(self.main_Window)
        self.bottom_Frame = tkinter.Frame(self.main_Window)

        self.enemy_Variable = tkinter.StringVar()
        self.player_Variable = tkinter.StringVar()
        self.label_1 = tkinter.Label(self.top_Frame, textvariable=self.enemy_Variable)
        self.label_2 = tkinter.Label(self.top_Frame, textvariable=self.player_Variable)

        self.label_1.pack(side='top')
        self.label_2.pack(side='top')

        self.button_1 = tkinter.Button(self.bottom_Frame, text='fight', command=self.fight_Callback)
        self.button_2 = tkinter.Button(self.bottom_Frame, text='Flee', command=self.flee_Callback)

        self.button_1.pack(side='top')
        self.button_2.pack(side='top')

        self.top_Frame.pack()
        self.bottom_Frame.pack()

        tkinter.mainloop()

    def fight_Callback(self):
        print('hi')
        # player_Variable, enemy_Variable = Combat.initiation(self.__player)
        value = 'deez'
        self.enemy_Variable.set(value)
        self.player_Variable.set(value)

    def flee_Callback(self):
        save(self.__player)
        self.main_Window.destroy()
