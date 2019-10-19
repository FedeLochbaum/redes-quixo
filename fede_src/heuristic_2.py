points = [
  [5, 1, 3 ,1 ,5],
  [1, 2, 1, 2, 1],
  [3, 1, 9, 1, 3],
  [1, 2, 1, 2, 1],
  [5, 1, 3, 1, 5]
]

def heuristic_2(game, player = 'X', oponent = 'O'):
  res = 0
  for i_row in range(len(game.board)):
    for i_column in range(len(game.board[i_row])):
      value = game.board[i_row][i_column].symbol_to_show()
      if(value == player):
        res += points[i_row][i_column]
  return res