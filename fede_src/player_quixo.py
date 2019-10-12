from quixo import Quixo
from copy import deepcopy
import timeit
from alpha_beta import alphabeta

time_millis = lambda: 1000 * timeit.default_timer()

class QuixoPlayer:
  def __init__(self, search_depth = 3, timeout = 10.):
    self.game = Quixo()
    self.player = None
    self.timer_threshold = timeout
    self.search_depth = search_depth
    self.time_left = None
  
  def set_player(self, player):
    self.player = player
  
  def playerPlay(self):
    if self.player == None: self.set_player('X')
    move_start = time_millis()
    time_left = lambda : self.timer_threshold - (time_millis() - move_start)

    move = self.get_move(time_left)
    self.game.apply_move(self.player, move)
    return move

  def oponentPlay(self, oponent, move):
    if self.player == None: self.set_player('O')
    self.game.apply_move(oponent, move)

  def is_time_over(self):
    if self.time_left() < self.timer_threshold:
      raise SearchTimeout()

  def get_move(self, time_left):
    self.time_left = time_left
    best_move = (-1, -1)
    depth = 1
    try:
      while (True):
        move = alphabeta(self.game, depth)
        if move is not (-1, -1):
          best_move = move
          depth += 1 
          if self.time_left() < self.timer_threshold:
            return best_move

    except SearchTimeout:
      return best_move

class SearchTimeout(Exception):
  pass