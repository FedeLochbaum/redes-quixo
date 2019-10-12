from math import inf
from copy import deepcopy

MAX = 1
MIN = -1

def alphabeta(node, depth, alpha, beta, player, h):
  if depth == 0 or node.game_over():
    return h(node)
  if player == MAX:
    value = -inf
    for move in node.all_valid_moves('X'):
      child = deepcopy(node)
      child.apply_move('X', move)
      value = max(value, alphabeta(child, depth - 1, alpha, beta, -player, h))
      alpha = max(alpha, value)
      if alpha >= beta:
        break # beta cut - off
    return value
  else:
    value = inf
    for move in node.all_valid_moves('O'):
      child = deepcopy(node)
      child.apply_move('O', move)
      value = min(value, alphabeta(child, depth - 1, alpha, beta, -player, h))
      beta  = min(beta, value)
      if alpha >= beta:
        break # alpha cut - off
  return value
