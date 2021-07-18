from tkinter import BOTH, StringVar, Label, Entry, TOP
from tkinter.ttk import Frame, Button, Style
from data_Handling import save
from game import Combat, create_Character


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
        self.location_Value = StringVar()

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

    def get_Location(self):
        return self.location_Value

    def set_Name_Value(self):
        self.name_Value.set(self.__player.get_Name())

    def set_exp_Value(self):
        self.exp_Value.set(self.__player.get_Exp())

    def set_hp_Value(self):
        self.hp_Value.set(self.__player.get_Hp())

    def set_str_Value(self):
        self.str_Value.set(self.__player.get_Str())

    def set_mp_Value(self):
        self.mp_Value.set(self.__player.get_Mp())

    def set_Location_Value(self):
        self.location_Value.set(self.__player.get_Location())

    def set_All_Values(self):
        print(self.__player.get_Name())
        self.name_Value.set(self.__player.get_Name())
        self.exp_Value.set(self.__player.get_Exp())
        self.hp_Value.set(self.__player.get_Hp())
        self.str_Value.set(self.__player.get_Str())
        self.mp_Value.set(self.__player.get_Mp())

    def initUI(self):
        self.style.theme_use("default")

        self.master.title("Test")
        self.pack(fill=BOTH, expand=1)

        background = Label(self, bg='SlateGray4', width=300, height=300)
        background.pack(side=TOP)

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

    def explore_Callback(self):
        Combat.initiation(self.__player)

    def quit_Callback(self):
        save(self.__player)
        exit()


# Gui to create character if not found in save file
class CharacterCreationGui(Frame):
    def __init__(self):
        super().__init__()

        self.style = Style()
        self.name_Entry = StringVar()

        self.initUI()

    def initUI(self):
        background = Label(self, bg='SlateGray4', width=300, height=300)
        background.pack(side=TOP)

        self.master.title("Character Creation: ")
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.description = Label(self, text='Please enter a name for your character: ')
        self.description.place(x=50, y=50)

        self.name_Entry = Entry(self)
        self.name_Entry.place(x=90, y=75)

        self.create_Button = Button(self, text='Create', command=self.create_Callback)
        self.create_Button.place(x=120, y=100)

    def create_Callback(self):
        Name = self.name_Entry.get()
        create_Character(Name, 100, 0, 10, 10, 'start')
        self.master.destroy()


class DeathScreenGui(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("")

        background = Label(self, bg='SlateGray4', width=300, height=300)
        background.pack(side=TOP)

        self.label_1 = Label(self, text='You have died...')
        self.label_1.place(x=50, y=50)

        self.button_1 = Button(self, text="Exit", command=self.button_Callback)
        self.button_1.place(x=25, y=25)

    def button_Callback(self):
        exit()
