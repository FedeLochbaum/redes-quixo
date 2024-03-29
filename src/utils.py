import random
import timeit

time_millis = lambda: 1000 * timeit.default_timer()

def all_the_same_elements(elements, player = None):
  return all(x == y and x != 'W' and y != 'W' for x, y in zip(elements, elements[1:])) if(player == None) else all(x == y and x == player and y == player for x, y in zip(elements, elements[1:]))

def to_simple_structure(game):
  return list(map(lambda row: to_simplify(row), game.board))

def to_simplify(elems):
  return list(map(lambda cell: cell.symbol_to_show(), elems))

def count_of_neighbors(elems, player):
  # elems [Cell]
  res = 0
  for cell in elems:
    if cell.symbol_to_show() == player:
      res += 1
    else:
      res = 0
  return res

max_size = 5
list(map(lambda x: (x * -1, 0), range(max_size)))
north = list(map(lambda x: (x * -1, 0), range(max_size)))
east = list(map(lambda x: (0, x), range(max_size)))
south = list(map(lambda x: (x, 0), range(max_size)))
west = list(map(lambda x: (0, x * -1), range(max_size)))
neast = list(map(lambda x: (x * -1, x), range(max_size)))
seast = list(map(lambda x: (x, x), range(max_size)))
swest = list(map(lambda x: (x, x * -1), range(max_size)))
nwest = list(map(lambda x: (x * -1, x), range(max_size)))
cardinals = [north, east, south, west, neast, seast, swest, nwest]

def check(player, pos, game):
  return check_positions(player, pos, game)

def check_positions(player, pos, game):
  for cardinal in cardinals:
    if has_cardinal(player, cardinal, pos, game):
      return True
  return False

def has_cardinal(player, cardinal, pos, game):
  won = True
  for tup in cardinal:
    x, y = (pos[0] + tup[0], pos[1] + tup[1])
    won &= game[x][y].symbol == player
  return won

def random_heuristic(game, player = 'X', oponent = 'O'):
  return random.random()

def play(player1, player2, timeout = 10000.):
  start_time = time_millis()
  current_time = start_time
  while(not player1.game.game_over()):
    player2.oponentPlay(player1.playerPlay())
    player1.oponentPlay(player2.playerPlay())
    current_time = time_millis() 
    if (current_time - start_time) > timeout:
      raise Exception('Timeout')

  return player1.game
