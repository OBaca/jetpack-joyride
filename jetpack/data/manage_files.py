
''' This function saves the coin amount the player have to a file. '''
def update_coins(coins):
    with open('coins.txt', 'w') as file:
        file.write(str(coins))


''' This function read from the coins file to see the amount of coins the player have. '''
def read_coins():
    with open('coins.txt', 'r') as file:
        return file.read()


''' This function returns the amount of coins the player have '''
def get_coins():
    try:
        coins = int(read_coins())
    except:
        coins = 0
    return coins


''' This function saves the high score to a file. '''
def update_high_score(high_score, score):
    if high_score < score:
        high_score = score
    with open('high_score.txt','w') as file:
        file.write(str(high_score))
    return high_score


''' This function return the high score of the player. '''
def get_high_score():
    try:
        high_score = int(read_high_score())
    except:
        high_score = 0
    return high_score


''' This high score check and return the highest score from a file. '''
def read_high_score():
    with open("high_score.txt", 'r') as file:
        return file.read()


''' This function return the skin the user have. '''
def read_skin():
    with open('skins.txt', 'r') as file:
        return file.read()


''' This function add the new skin to the skins the user have. '''
def buy_skin(skin):
    skins = read_skin()
    with open('skins.txt','w') as file:
        file.write(skins + '\n' + str(skin))


''' This function check if the user have the skin given as a paramater. '''
def check_skins_inventory(skin):
    with open('skins.txt', 'r') as file:
        return True if skin in file.read() else False

