import pickle


# Save character stats
def save(plyr):
    FILE_NAME = 'saveFile.txt'
    again = True
    output_file = open(FILE_NAME, 'wb')

    while again:
        pickle.dump(plyr, output_file)
        again = False

    output_file.close()
    print("Data was written to ", FILE_NAME)


# Load character stats
def load():
    FILE_NAME = 'saveFile.txt'
    end_of_file = False
    player_Exists = False
    player_Save = None
    input_file = open(FILE_NAME, 'rb')

    while not end_of_file:
        try:
            player_Save = pickle.load(input_file)
            player_Exists = True
        except EOFError:
            end_of_file = True

    input_file.close()
    return player_Save, player_Exists
