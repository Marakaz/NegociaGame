


print("Welcome to the 'Negocia' - the land of Knights and Amazons")

hero = None
hero_choosen = None
start_a_game = None

# Starting a game.

while True:
    start_a_game = input('Would you like to try yourself on fileds of the Negocia?\n'
                         'press Y for go on or N to quit >> ').upper()
    if start_a_game == 'Y':
        print("Great! Let's begin.")
        break
    elif start_a_game == "N":
        print('Goodbye then. Hope to see you soon!')
        break
    else:
        print('You can choose only between Y or N')
        print("\n")
        start_a_game = None
        continue

# Choosing the hero.

if start_a_game == 'Y':
    while True:
        if True:
            hero_choosen = input("Choose your hero: Knight or Amazon? >> ").capitalize()
            if hero_choosen == "Knight":
                print("Draw your sword Knight! From now your name is Anos!")
                hero = knight()
                break
            elif hero_choosen == "Amazon":
                ''' Untag when Amazon option will be avaiable.
                 print("Raise your spear, Amazon! From know you should call yourself Samira!")
                 hero = amazon()
                break'''
                print('Sorry, the Amazon is not avaiable yet.')
            else:
                print("There\'s some error! Try to write the name of hero with capital letter.")






