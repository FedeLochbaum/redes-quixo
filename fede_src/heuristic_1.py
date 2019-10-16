from utils import count_of_neighbors

strategic_points = [(0, 0), (0, 4), (4, 4), (4, 0), (0, 2), (2, 4), (4, 2), (2, 0)]

def count_of_tokens(game):
  res = (0, 0)
  for i_row in range(len(game.board)):
    for i_column in range(len(game.board[i_row])):
      value = game.board[i_row][i_column].symbol_to_show()
      if(value == 'O'):
        res = (res[0] + 1, res[1])

      if(value == 'X'):
        res = (res[0], res[1] + 1)
  return res

def count_of_strategic_points(game, player):
  return sum(map(lambda pair: 1 if game.board[pair[0]][pair[1]].symbol_to_show() == player else 0, strategic_points), 0)

def in_center(game, player):
  return game.board[2][2].symbol_to_show() == player

def max_count_of_neighbors_in_rows(game, player):
  return max([count_of_neighbors(row, player) for row in game.board])

def max_count_of_neighbors_in_columns(game, player):
  return max([count_of_neighbors(column, player) for column in game.columns()])

def max_count_of_neighbors_in_diagonals(game, player):
  return max([count_of_neighbors(game.left_diagonal(), player), count_of_neighbors(game.right_diagonal(), player)])

def max_count_of_neighbors(game, player):
  mconir = max_count_of_neighbors_in_rows(game, player)
  mconic = max_count_of_neighbors_in_columns(game, player)
  mconid = max_count_of_neighbors_in_diagonals(game, player)
  return max([mconir, mconic, mconid])

def heuristic_1(game, player, oponent):
  player_index = 0 if player == 'O' else 1
  oponent_index = 1 if player_index == 0 else 0

  cot = count_of_tokens(game)
  count_of_tokens_value = (cot[player_index] - cot[oponent_index]) * 1.2 # I think that this value has 20% more importance
  cosp = count_of_strategic_points(game, player)
  center_importance = 16 * (1 if in_center(game, player) else 0)
  return count_of_tokens_value + center_importance + max_count_of_neighbors(game, player) * max(1, cosp)