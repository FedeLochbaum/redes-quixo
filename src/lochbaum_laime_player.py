from quixo import Quixo
from copy import deepcopy
import timeit
import random
from math import inf
from copy import deepcopy
from utils import to_simple_structure, count_of_neighbors, random_heuristic
from heuristic_1 import heuristic_1
from heuristic_2 import heuristic_2

time_millis = lambda: 1000 * timeit.default_timer()

class QuixoPlayer:
  def __init__(self, search_depth = 2, timeout = 50., heuristic = heuristic_1):
    self.game = Quixo()
    self.player = None
    self.timer_threshold = timeout
    self.search_depth = search_depth
    self.heuristic = heuristic
    self.time_left = None
  
  def set_player(self, player):
    self.player = player
  
  def playerPlay(self):
    if self.player == None: self.set_player('X')
    move_start = time_millis()
    # time_left represent the left time, calculating the passed time (time_millis() - move_start)
    time_left = lambda : self.timer_threshold - (time_millis() - move_start)

    focus, target = self.get_move(time_left)
    self.game.apply_move(self.player, (focus, target))
    return focus + 1, target + 1 # To support the standard order

  def oponentPlay(self, move):
    focus, target = move
    if self.player == None: self.set_player('O')

    oponent_player = 'X' if self.player == 'O' else 'O'

    if not (focus -1, target - 1) in self.game.all_valid_moves(oponent_player): raise Exception('Invalid move')

    self.game.apply_move(oponent_player, (focus - 1, target - 1)) # To support the standard order

  def is_time_over(self):
    if self.time_left() <= 0:
      raise SearchTimeout()

  def get_move(self, time_left):
    self.time_left = time_left
    best_move = self.game.all_valid_moves(self.player)[0]
    depth = 1
    try:
      while (depth <= self.search_depth):
        move = self.alphabeta(self.game, depth, self.player)
        best_move = move
        depth += 1
        if self.time_left() <= 0:
          return best_move
      return best_move

    except SearchTimeout:
      return best_move
  
  def alphabeta(self, game, depth, player, alpha = -inf, beta = inf):
    if player == 'X':
      legal_moves = game.all_valid_moves('X')
      if not legal_moves:
        return (-1, -1)
      best_current_move = legal_moves[0]
      for move in legal_moves:
        self.is_time_over()
        child = deepcopy(game)
        child.apply_move('X', move)
        score = self.max_value(child, depth - 1, alpha, beta)
        if score > alpha:
          alpha = score
          best_current_move = move
      return best_current_move
    else:
      legal_moves = game.all_valid_moves('O')
      if not legal_moves:
        return (-1, -1)
      best_current_move = legal_moves[0]
      for move in legal_moves:
        self.is_time_over()
        child = deepcopy(game)
        child.apply_move('O', move)
        score = self.min_value(child, depth - 1, alpha, beta)
        if score < beta:
          beta = score
          best_current_move = move
      return best_current_move

  def min_value(self, game, depth, alpha, beta):
    if depth == 0:
      return self.heuristic(game)
    legal_moves = game.all_valid_moves('X')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('X', move)
      score = self.max_value(child, depth - 1, alpha, beta)
      if score < beta:
        beta = score
        if beta <= alpha:
          break
    return beta

  def max_value(self, game, depth, alpha, beta):
    if depth == 0:
      return self.heuristic(game)
    legal_moves = game.all_valid_moves('O')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('O', move)
      score = self.min_value(child, depth - 1, alpha, beta)
      if score > alpha:
        alpha = score 
        if alpha >= beta:
          break       
    return alpha

class SearchTimeout(Exception):
  pass
