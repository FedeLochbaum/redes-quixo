from quixo import Quixo
from copy import deepcopy
import timeit
from math import inf
from copy import deepcopy

MAX = 1
MIN = -1

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
        move = self.alphabeta(self.game, depth, self.player)
        if move is not (-1, -1):
          best_move = move
          depth += 1
          if self.time_left() < self.timer_threshold:
            return best_move

    except SearchTimeout:
      return best_move
  
  def alphabeta(self, game, depth, player, h, alpha = -inf, beta = inf):
    if player == MAX:
      legal_moves = game.all_valid_moves('X')
      if not legal_moves:
        return (-1, -1)
      self.best_current_move = legal_moves[0]
      for move in legal_moves:
        self.is_time_over()
        child = deepcopy(game)
        child.apply_move('X', move)
        score = self.min_value(child, depth - 1, h, alpha, beta)
        if score > alpha:
          alpha = score
          self.best_current_move = move
      return self.best_current_move
    else:
      legal_moves = game.all_valid_moves('O')
      if not legal_moves:
        return (-1, -1)
      self.best_current_move = legal_moves[0]
      for move in legal_moves:
        self.is_time_over()
        child = deepcopy(game)
        child.apply_move('O', move)
        score = self.max_value(child, depth - 1, h, alpha, beta)
        if score < beta:
          beta = score
          self.best_current_move = move
      return self.best_current_move

  def min_value(self, game, depth, h, alpha, beta):
    if depth == 0:
      return h(game)
    legal_moves = game.all_valid_moves('O')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('O', move)
      score = self.max_value(child, depth - 1, h, alpha, beta)
      if score < beta:
          beta = score 
          if beta <= alpha:
              break       
    return beta

  def max_value(self, game, depth, h, alpha, beta):
    if depth == 0:
      return h(game)
    legal_moves = game.all_valid_moves('X')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('X', move)
      score = self.min_value(child, depth - 1, h, alpha, beta)
      if score > alpha:
          alpha = score 
          if alpha >= beta:
            break       
    return alpha

class SearchTimeout(Exception):
  pass