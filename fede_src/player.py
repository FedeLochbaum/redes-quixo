from quixo import Quixo
from copy import deepcopy
import timeit
from math import inf
from copy import deepcopy

def heuristic(game):
  # Simple heuristic
  return 2

time_millis = lambda: 1000 * timeit.default_timer()

class QuixoPlayer:
  def __init__(self, search_depth = 3, timeout = 100.):
    self.game = Quixo()
    self.player = None
    self.timer_threshold = timeout
    self.search_depth = search_depth
    self.time_left = None
  
  def set_player(self, player):
    self.player = player
  
  def playerPlay(self):
    if self.player == None: self.set_player('O')
    move_start = time_millis()
    # time_left represent the left time, calculating the passed time (time_millis() - move_start)
    time_left = lambda : self.timer_threshold - (time_millis() - move_start)

    move = self.get_move(time_left)
    self.game.apply_move(self.player, move)
    return move

  def oponentPlay(self, move):
    if self.player == None: self.set_player('X')

    if move[0] == -1 or move[1] == -1: raise Exception('Invalid move')
    oponent_player = 'O' if self.player == 'X' else 'X'
    self.game.apply_move(oponent_player, move)

  def is_time_over(self):
    if self.time_left() <= 0:
      raise SearchTimeout()

  def get_move(self, time_left):
    self.time_left = time_left
    best_move = self.game.all_valid_moves(self.player)[0]
    depth = 1
    try:
      while (True):
        move = self.alphabeta(self.game, depth, self.player, heuristic = heuristic)
        best_move = move
        depth += 1
        if self.time_left() <= 0:
          return best_move

    except SearchTimeout:
      return best_move
  
  def alphabeta(self, game, depth, player, heuristic, alpha = -inf, beta = inf):
    if player == 'X':
      legal_moves = game.all_valid_moves('X')
      if not legal_moves:
        return (-1, -1)
      best_current_move = legal_moves[0]
      for move in legal_moves:
        self.is_time_over()
        child = deepcopy(game)
        child.apply_move('X', move)
        score = self.min_value(child, depth - 1, heuristic, alpha, beta)
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
        score = self.max_value(child, depth - 1, heuristic, alpha, beta)
        if score < beta:
          beta = score
          best_current_move = move
      return best_current_move

  def min_value(self, game, depth, heuristic, alpha, beta):
    if depth == 0:
      return heuristic(game)
    legal_moves = game.all_valid_moves('O')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('O', move)
      score = self.max_value(child, depth - 1, heuristic, alpha, beta)
      if score < beta:
        beta = score 
        if beta <= alpha:
          break       
    return beta

  def max_value(self, game, depth, heuristic, alpha, beta):
    if depth == 0:
      return heuristic(game)
    legal_moves = game.all_valid_moves('X')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('X', move)
      score = self.min_value(child, depth - 1, heuristic, alpha, beta)
      if score > alpha:
        alpha = score 
        if alpha >= beta:
          break       
    return alpha

class SearchTimeout(Exception):
  pass


player1 = QuixoPlayer()
player2 = QuixoPlayer()
player1.game.show()

while(not player1.game.game_over()):
  player2.oponentPlay(player1.playerPlay())
  player1.oponentPlay(player2.playerPlay())
  player1.game.show()
