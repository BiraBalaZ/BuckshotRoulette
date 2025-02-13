from classes import Game, Entity, Player, Dealer, Shotgun

# Creating Game object
game = Game()

# Creating Player object
player = Player(Entity)
player.life = initialLife

assert player.alive == True

# Creating Dealer object
dealer = Dealer(Entity)
dealer.life = initialLife
assert dealer.alive == True

# Creating Shotgun object
shotgun = Shotgun()

# TODO: Checar se a Shotgun atira e perde um cartucho

# TODO: Checar se o Player perde vida

# TODO: Checar se o Dealer perde vida

# TODO: Checar se o Player morre

# TODO: Checar se o Dealer morre


# Checking tests results
print("Passed all tests! =D")