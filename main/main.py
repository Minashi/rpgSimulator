from gui import MenuGui, CharacterCreationGui
from tkinter import Tk
from data_Handling import load

# TODO
#   Leveling system
#   add death screen eventually (192 fix)
#   Fix kill method in Enemy class
#   Make a load menu showing all available saves with a list box
#   Allow more then 1 save
#   Figure out why name is not printing right on menu (HP is being printed as name for some reason)
#   Add ability to heal

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
