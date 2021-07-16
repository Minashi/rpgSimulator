import game
import data_Handling
import command_Thread
import threading
import sys


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


def main():
    player, player_Exists = data_Handling.load()
    while player_Exists:
        game.MenuGui(player)
    else:
        game.CharacterCreationGui()
        main()
        # game.MenuGui(player)

# Check if thread is active if not close game


def thread_Check(thread_1):
    thread_2 = threading.Thread(target=thread_Check)
    thread_2.start()
    while thread_1.is_alive():
        pass
    else:
        exit()
        sys.exit()


def start_Thread():
    thread = command_Thread.CommandClass(None)
    thread_1 = threading.Thread(target=thread.main_Thread)
    thread_1.start()
    thread.set_Name(thread_1)
    thread_Check(thread_1)


start_Thread()
main()


def ADD10():
    while True:
        ADD10()
