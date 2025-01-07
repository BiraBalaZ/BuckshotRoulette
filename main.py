from time import sleep
from os import system
import random
system('cls')
playerLife = 3
iaLife = 3
maxLife = 5
turn = 'Player'
def printLife():
    sleep(1)
    print('YOU')
    print(':alta_tensão:' * playerLife)
    print()
    sleep(1)
    print('HE')
    print(':alta_tensão:' * iaLife)
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
print(f'Uma arma está na mesa, mostram-se {realCount} cartuchos verdadeiros e {festimCount} cartuchos falsos.')
sleep(1)
print('Eles entram na arma aleatoriamente.')
sleep(1)
print('Boa sorte.')
sleep(2)
while iaLife > 0 or playerLife > 0 or len(ammo) > 0:
    printLife()
    if turn == 'Player':
        escolha = int(input('[0] Atirar em você\n[1] Atirar NELE\n>>>'))
        system('cls')
    elif turn == 'IA':
        escolha = int(random.randrange(0, 2))
        system('cls')
    # Atirando no Jogador
    if escolha == 0:
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
    if escolha == 1:
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
    del ammo[0]
    printLife()
    if iaLife == 0:
        print('Você venceu\nFim de Jogo')
        break
    elif playerLife == 0:
        print('Você perdeu...\nFim de Jogo')
        break
    print('Fim da rodada\nPróxima rodada!')
    continue
