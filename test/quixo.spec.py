import unittest
from src.quixo import Quixo

class QuixoTest(unittest.TestCase):

  def test_the_board_is_created_empty(self):
    quixo = Quixo()
    self.assertTrue(isInInitialState(quixo))


def isInInitialState(game):
  return all(map(game.board), lambda row: all(map(lambda cell: cell.symbol == 'empty')))

if __name__ == '__main__':
  unittest.main()
