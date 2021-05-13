import random
import threading
from time import sleep

leave = False


class TitleScreen:
    @staticmethod
    def loadGame():
        SaveRequest.loadGame()
        sleep(1)
        prompt()

    @staticmethod
    def aboutPage():
        print("\n###########################")
        print("Created by Brandon Gonzalez\n")
        print("press enter to return...")
        print("###########################")
        input(">")
        mainLoop()

    @staticmethod
    def leaveGame():
        print("Would you like to leave the game?")
        action = input(">")

        if action.lower() == 'yes':
            SaveRequest.saveGame()
            exit()
        else:
            mainLoop()


class SaveRequest:

    @staticmethod
    def loadGame():
        try:
            saveFile = open('saveFile.txt', 'r')
            read = saveFile.readline()

            if read != '':
                print("Would you like to load your save?")
                action = input(">")
                if action.lower() == 'yes':
                    print("\nopening save...")
                    name = read
                    classType = saveFile.readline()
                    currency = saveFile.readline()

                    currency = currency.rstrip('\n')
                    currency = int(currency)

                    name = name.rstrip('\n')
                    classType = classType.rstrip('\n')

                    global player
                    player = Avatar(name, classType, currency)
                    sleep(1)
                    print("save opened...")
                else:
                    return

        except IOError:
            print("You do not have any saved games...")
            print("Starting new game...\n")
            characterCreation()

    @staticmethod
    def saveGame():
        print("saving game...")
        currency = str(player.currency)
        newSaveFile = open('saveFile.txt', 'w')

        newSaveFile.write(player.name)
        newSaveFile.write('\n')
        newSaveFile.write(player.classType)
        newSaveFile.write('\n')
        newSaveFile.write(currency)

        print("game saved...")
        newSaveFile.close()


class Avatar:
    def __init__(self, name, classType, currency):
        self.name = name
        self.classType = classType
        self.currency = currency
        # self.statusEffects = []

    def examineStats(self):
        print("########################################################################")
        print("\nName:", self.name, "Class:", self.classType)
        print("\n-Inventory:", "\n\tItem1:", "\n\tItem2:", "\n\tCurrency:", self.currency)
        print("Status Effects:")
        print("\nType anything to return to the game.")
        print("########################################################################")
        input(">")

    def inventory(self):
        pass


class Combat:
    @staticmethod
    def encounter():
        pass


class Locations:
    @staticmethod
    def travel():
        pass


def title_Screen():
    print("####################################")
    print("#######    RPG Simulator     #######")
    print("#######        Play          #######")
    print("#######        About         #######")
    print("#######        Leave         #######")
    print("####################################")
    action = input(">")
    while action.lower() != 'play' and action.lower() != 'about' and action.lower() != 'leave':
        print("Unrecognized input. Please try again...")
        action = input(">")
    else:
        if action.lower() == 'play':
            TitleScreen.loadGame()
        elif action.lower() == 'about':
            TitleScreen.aboutPage()
        elif action.lower() == 'leave':
            TitleScreen.leaveGame()


def characterCreation():
    print("What is your name")
    name = input(">")
    print("What class you want nerd 'warrior, mage, assassin'")
    classType = input(">")
    global player
    player = Avatar(name, classType, 500)
    SaveRequest.saveGame()


def prompt():
    print("\n   What would you like to do?")
    print("#####    Travel           #####")
    print("#####    Inventory        #####")
    print("#####    Examine Stats    #####")
    # print("#####    options          #####")
    print("#####    Quit             #####")
    action = input(">")
    if action.lower() in ['travel']:
        Locations.travel()
    elif action.lower() in ['inventory']:
        player.inventory()
    elif action.lower() in ['examine', 'examine stats']:
        player.examineStats()
    # elif action.lower() in ['help', 'options']:
    #     pass
    elif action.lower() in ['exit', 'leave', 'quit']:
        print("Are you sure you want to quit?")
        action = input(">")
        if action.lower() == 'yes':
            global leave
            leave = True
            return


def statsThread():
    pass


def mainLoop():
    title_Screen()
    while not leave:
        prompt()
    else:
        SaveRequest.saveGame()
        exit()


player = Avatar(0, 0, 0)
thread = threading.Thread(target=statsThread())
mainLoop()
