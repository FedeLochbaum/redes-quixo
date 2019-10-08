def all_the_same_elements(elements):
  return all(x == y for x, y in zip(elements, elements[1:]))

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