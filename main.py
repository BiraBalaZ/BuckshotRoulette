from time import sleep
from os import system
from functions import printLife
import random

playerLife = 3
iaLife = 3

while (iaLife > 0 or playerLife > 0) and len(ammo) > 0:
    system('cls')
    turn = 'Player'
    choice = None

    ammo = random.randrange(1, 8)

    if ammo == 1:
        ammo = ['Real', 'Festim', 'Real', 'Festim', 'Real', 'Festim']
    elif ammo == 2:
        ammo = ['Festim', 'Real', 'Festim']
    elif ammo == 3:
        ammo = ['Real', 'Festim', 'Real', 'Real']
    elif ammo == 4:
        ammo = ['Real', 'Festim']
    elif ammo == 5:
        ammo = ['Real', 'Festim', 'Real', 'Real']
    elif ammo == 6:
        ammo = ['Festim', 'Festim', 'Real', 'Real']
    elif ammo == 7:
        ammo = ['Festim', 'Festim', 'Festim', 'Festim', 'Real', 'Real']

    random.shuffle(ammo)
    print(ammo)

    festimCount = ammo.count('Festim')
    realCount = ammo.count('Real')

    sleep(1)
    print(f'{realCount} cartuchos verdadeiros e {festimCount} cartuchos falsos.')
    sleep(2)

    # while (iaLife > 0 or playerLife > 0) and len(ammo) > 0:
    printLife(playerLife, iaLife)

    if turn == 'Player':
        choice = int(input('[0] Atirar em você\n[1] Atirar NELE\n>>>'))
        system('cls')
    elif turn == 'IA':
        festimCount = ammo.count('Festim')
        realCount = ammo.count('Real')
        
        # Fazendo ele "contar" quantas balas foram
        if festimCount > 0 and realCount == 0:
            choice = 1
        elif festimCount == 0 and realCount > 0:
            choice = 0
        else:
            choice = int(random.randrange(0, 2))
        system('cls')

    # Atirando no Jogador
    if choice == 0:
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
    elif choice == 1:
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

    # If the life of one of them is zero, the game ends
    if iaLife == 0:
        print('Você venceu\nFim de Jogo')
        break
    elif playerLife == 0:
        print('Você perdeu...\nFim de Jogo')
        break

    # If the shotgun ammo is zero, the game restart with other Ammo Set
    # print('Fim da rodada\nPróxima rodada!')
    # continue

    sleep(3)
    system('cls')
    print('Sem balas.\nPróxima rodada.')
