from gui import MenuGui, CharacterCreationGui
from tkinter import Tk
from data_Handling import load

# TODO
#   Add items and rarities
#   Add loot system
#   Leveling system
#   add death screen eventually
#   Fix kill method in Enemy class
#   Make a load menu showing all available saves with a list box
#   Allow more then 1 save
#   Check why player keeps getting roasted by enemies
#   Fix throwing error on line 274

list_Of_Threads = []


def main():
    player, player_Exists = load()
    while player_Exists:
        root = Tk()
        root.geometry("300x300+500+250")
        app = MenuGui(player)
        root.mainloop()
    else:
        root = Tk()
        root.geometry("300x300+500+250")
        app = CharacterCreationGui()
        root.mainloop()
        main()


main()
