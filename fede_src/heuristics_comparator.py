from utils import random_heuristic, play
from heuristic_1 import heuristic_1
from heuristic_2 import heuristic_2
from player import QuixoPlayer
import matplotlib.pyplot as plt

heuristic1 = heuristic_1 # Red
heuristic2 = heuristic_2 # Blue

timeouts = sorted(set([float(x) if (x % 50  == 0) else 50 for x in range(50, 1001)]))
search_depths = list([x for x in range(1, 6)])

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
      plt.plot(timeout, depth, c='red', marker = 'o', linewidth=1.0)
    else:
      if (game.game_over('X')): # If X is the winner
        plt.plot(timeout, depth, c='blue', marker = 'o', linewidth=1.0)
      else: # Tie
        plt.plot(timeout, depth, c='black', marker = 'o', linewidth=1.0)


plt.show()