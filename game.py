import random
import pickle
import tkinter
import tkinter.messagebox

locations = ['menu', 'explore']
active_Enemy_List = []
enemy_Attributes = {'Goblin': ['Goblin', 100, 10, 10],
                    'Ogre': ['Ogre', 200, 50, 0]
                    }


class Avatar:
    def __init__(self, Name, Hp, Exp, Str, Mp, location):
        self.__Name = Name
        self.__Hp = Hp
        self.__Exp = Exp
        self.__Str = Str
        self.__Mp = Mp
        self.__Location = location

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

    def explore(self, location):
        if location in locations:
            self.set_Location(location)
        else:
            print('Invalid Location')

    # def __str__(self):
    #     return self.__Name + self.__Hp + self.__Exp + self.__Str + self.__Mp


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

    # def __str__(self):
    #     return self.__Name + self.__Hp + self.__Exp + self.__Str + self.__Mp


class Combat:
    @staticmethod
    def initiation(player, npc):
        print("Player is ", player.get_Name())
        print("Enemy is ", npc.get_Name())


def create_Character(Name, Hp, Exp, Str, Mp, location):
    player = Avatar(Name, Hp, Exp, Str, Mp, location)
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


class MenuGui:
    def __init__(self, player):
        self.player = player

        self.main_Window = tkinter.Tk()

        self.menu_Frame = tkinter.Frame(self.main_Window)

        self.explore_Button = tkinter.Button(self.menu_Frame, text='Explore', command=self.explore_Callback)
        self.character_Button = tkinter.Button(self.menu_Frame, text='Character', command=self.character_Callback)
        self.settings_Button = tkinter.Button(self.menu_Frame, text='Settings', command=self.settings_Callback)
        self.quit_Button = tkinter.Button(self.menu_Frame, text='Quit', command=self.quit_Callback)

        self.explore_Button.pack(side='top')
        self.character_Button.pack(side='top')
        self.settings_Button.pack(side='top')
        self.quit_Button.pack(side='top')

        self.menu_Frame.pack()

        tkinter.mainloop()

    @staticmethod
    def explore_Callback():
        pass

    def character_Callback(self):
        tkinter.messagebox.showinfo('Character', 'Name: ' + self.player.get_Name()
                                    + '\nHP: ' + str(self.player.get_Hp())
                                    + '\nEXP: ' + str(self.player.get_Exp())
                                    + '\nStr: ' + str(self.player.get_Str())
                                    + '\nMP: ' + str(self.player.get_Mp())
                                    + '\nLocation: ' + self.player.get_Location())

    @staticmethod
    def settings_Callback():
        pass

    def quit_Callback(self):
        save(self.player)
        exit()


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


class ExploreGui:
    def __init__(self):
        pass
