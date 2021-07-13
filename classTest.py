import game


# TODO
#   Add items and rarities
#   Add loot system
#   Leveling system


def main():
    player, player_Exists = game.load()
    while player_Exists:
        game.MenuGui(player)
    else:
        game.CharacterCreationGui()
        main()


main()
