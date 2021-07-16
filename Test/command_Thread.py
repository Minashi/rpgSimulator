import sys

commands_List = ['give_health', 'give_xp', 'kill', 'exit']


class CommandClass:
    def __init__(self, name):
        self.__threadName = name

    def set_Name(self, name):
        self.__threadName = name

    def main_Thread(self):
        while True:
            command = input('Enter command: ').lower()

            # Command to heal person
            # command to give lots of xp
            # command to kill person

            if command == commands_List[0]:

                print("Added health")
            elif command == commands_List[1]:

                print("Added xp")
            elif command == commands_List[2]:

                print("Killed player and closed game")
            elif command == commands_List[3]:
                print("Closing game")
                self.close_Thread()
            else:
                print("Command unrecognized")

    @staticmethod
    def close_Thread():
        # main.close_Game()
        sys.exit()
