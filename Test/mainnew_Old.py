import game
from tkinter import Tk
import data_Handling

# TODO
#   Add items and rarities
#   Add loot system
#   Leveling system
#   add death screen eventually line 153
#   Fix invisible label on fightGui
#   Fix kill method in Enemy class
#   Battle class broken what da friq is happening game crashes (Turns out it was because I was multithreading)
#   Create a multithread to allow me to enter commands to heal character
#   Create a thread to check if threads are active, if not close game
#   Why does the GUI not respond when there is more then 1 thread
#   It seems threads and tkinter events don't mix
#   Probably have to cancel the command_Thread idea
#   Make a load menu showing all available saves with a list box
#   Allow more then 1 save
#   Check why player keeps getting roasted by enemies
#   Fix throwing error on line 274

list_Of_Threads = []


def main():
    player, player_Exists = data_Handling.load()
    while player_Exists:
        root = Tk()
        root.geometry("300x300+500+250")
        app = game.MenuGui(player)
        root.mainloop()
    else:
        game.CharacterCreationGui()
        main()
        # game.MenuGui(player)


# Check if thread is active if not close game


# def thread_Check():
#     error_Check = False
#
#     while not error_Check:
#         for thread in list_Of_Threads:
#             if thread.is_alive():
#                 pass
#             else:
#                 error_Check = True
#
#
# def append_Thread(thread):
#     list_Of_Threads.append(thread)
#     print("Thread Appended")
#
#
# def start_Thread():
#     thread = command_Thread.CommandClass(None)
#     thread_1 = threading.Thread(target=thread.main_Thread)
#     thread_1.start()
#
#     thread.set_Name(thread_1)
#     append_Thread(thread_1)
#
#     thread_2 = threading.Thread(target=thread_Check)
#     thread_2.start()
#
#     append_Thread(thread_2)


# Threads and tkinter events don't mix
# start_Thread()
main()
