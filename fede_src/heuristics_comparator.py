from utils import random_heuristic, play
from heuristic_1 import heuristic_1
from heuristic_2 import heuristic_2
from player import QuixoPlayer
import matplotlib.pyplot as plt

heuristic1 = heuristic_2 # Red
heuristic2 = heuristic_1 # Blue

timeouts = sorted(set([x if (x % 10  == 0) else 100 for x in range(100, 1001)]))
search_depths = list([x for x in range(1, 5)])

plt.ylabel('maximum depth')
plt.xlabel('maximum timeout')
plt.title('Heuristics results')

for depth in search_depths:
  for timeout in timeouts:
    print(' depth: ', depth, ' timeout: ', timeout)
    player1 = QuixoPlayer(depth, timeout, heuristic1) #  O
    player2 = QuixoPlayer(depth, timeout, heuristic2) #  X
    game = play(player1, player2)
    if (game.game_over('O')): # If O is the winner
      plt.plot([timeout], [depth], 'rx', c='r')
    else:
      if (game.game_over('X')): # If X is the winner
        plt.plot([timeout], [depth], 'rx', c='b')
      else: # Tie
        plt.plot([timeout], [depth], 'rx', c='black')

plt.show()