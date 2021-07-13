from game import Enemy
from game import create_Character
from game import load
from game import save
from game import Combat
from game import MenuGui
from game import CharacterCreationGui


# TODO
#   Add items and rarities
#   Add loot system
#   Leveling system

# def combat(player, npc):
#     pass


# combat(avatar_1, enemy_1)

# print(game.active_Enemy_List[0])
# print(avatar_1)
# print(enemy_1)
# game.Combat.initiation(avatar_1, enemy_1)

def character_Creation():
    CharacterCreationGui()
    main()


def main():
    player, player_Exists = load()
    while player_Exists:
        MenuGui(player)
    else:
        character_Creation()


main()
