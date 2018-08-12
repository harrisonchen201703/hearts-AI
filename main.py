import sys
print('Terminal encoding: {}'.format(sys.stdout.encoding))

from game import Game
from player import StupidPlayer, SimplePlayer

# These four players are playing the game
players = [SimplePlayer(1), StupidPlayer(2), StupidPlayer(3), SimplePlayer(4)]

# We are simulating n games accumulating a total score
scores = (0, 0, 0, 0)
nr_of_games = 7
print('We are playing {} game in total.'.format(nr_of_games))
for game_nr in range(nr_of_games):
    print('GAME {}'.format(game_nr))
    game = Game(players, verbose=False)
    scores = tuple(sum(x) for x in zip(scores, game.play()))

print(scores)
