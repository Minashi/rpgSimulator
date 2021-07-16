import sys
import time
import game
import data_Handling
import command_Thread
import threading

# TODO
#   Add items and rarities
#   Add loot system
#   Leveling system
#   add death screen eventually line 153
#   Fix invisible label on fightGui
#   Fix kill method in Enemy class
#   Battle class broken what da friq is happening game crashes
#   Create a multithread to allow me to enter commands to heal character
#   Create a thread to check if threads are active, if not close game
#   Why does the GUI not respond when there is more then 1 thread
#   It seems threads and tkinter events don't mix
#   Probably have to cancel the command_Thread idea

list_Of_Threads = []


def main():
    player, player_Exists = data_Handling.load()
    while player_Exists:
        game.MenuGui(player)
    else:
        game.CharacterCreationGui()
        main()
        # game.MenuGui(player)


# Check if thread is active if not close game


def thread_Check():
    error_Check = False

    while not error_Check:
        for thread in list_Of_Threads:
            if thread.is_alive():
                pass
            else:
                error_Check = True


def append_Thread(thread):
    list_Of_Threads.append(thread)
    print("Thread Appended")


def start_Thread():
    thread = command_Thread.CommandClass(None)
    thread_1 = threading.Thread(target=thread.main_Thread)
    thread_1.start()

    thread.set_Name(thread_1)
    append_Thread(thread_1)

    thread_2 = threading.Thread(target=thread_Check)
    thread_2.start()

    append_Thread(thread_2)


# Threads and tkinter events don't mix
# start_Thread()
main()
