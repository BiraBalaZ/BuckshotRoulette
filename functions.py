from time import sleep

def printLife(playerLife, iaLife):
    sleep(1)
    print('\nYOU')
    print('⚡' * playerLife)
    print()
    sleep(1)
    print('DEALER')
    print('⚡' * iaLife)
    print()
    sleep(1)

def shooting(target):

# Atirando no Jogador
    if target == 0:
        if turn == 'Player':
            print('Você aponta a arma para você mesmo')
        else:
            print('Ele aponta a arma para você')
        sleep(1)

        if ammo[0] == "Festim":
            print('Click')
            turn = 'Player'
        else:
            print('BANG')
            playerLife -= 1
            turn = 'IA'


    # Atirando Nele
    elif target == 1:
        if turn == 'Player':
            print('Você aponta a arma para Ele')
        else :
            print('Ele aponta a arma para si mesmo')
        sleep(1)

        if ammo[0] == "Festim":
            print('Click')
            turn = 'IA'
        else:
            print('BANG')
            iaLife -= 1
            turn = 'Player'

    sleep(2)

    # removing the first bullet
    if len(ammo) > 0:
        del ammo[0]