import unittest
from quixo_fede import Quixo

class QuixoTest(unittest.TestCase):
  def test_the_board_is_created_empty(self):
    expected_empty_structure = [['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W']]
    self.assertEqual(to_simple_structure(Quixo()), expected_empty_structure)

  def test_valid_borders(self):
    2
  
  def test_all_valid_moves(self):
    2

  def test_should_move_row(self):
    2

  def test_should_move_row_from_left(self):
    2
  
  def test_should_move_column_from_top(self):
    2

  def test_apply_move(self):
    2

def to_simple_structure(game):
  return list(map(lambda row: list(map(lambda cell: cell.symbol_to_show(), row)), game.board))

if __name__ == '__main__':
  unittest.main()
