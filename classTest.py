from game import Enemy
from game import create_Character
from game import load
from game import save
from game import Combat

# def combat(player, npc):
#     pass


# combat(avatar_1, enemy_1)

# print(game.active_Enemy_List[0])
# print(avatar_1)
# print(enemy_1)
# game.Combat.initiation(avatar_1, enemy_1)

def character_Creation():
    print("Hello! Welcome to my game. This is a test.")
    Name = input('Name: ')
    create_Character(Name, 10, 0, 10, 10)


def main():
    character_Creation()
    player = load()
    print(player.get_name())
    enemy = Enemy.rand_Enemy()
    Combat.initiation(player, enemy)


main()

# player = game.load()
#

