import unittest
from quixo_fede import Quixo, Cell

class QuixoTest(unittest.TestCase):
  def test_the_board_is_created_empty(self):
    expected_empty_structure = [['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'W']]
    self.assertEqual(to_simple_structure(Quixo()), expected_empty_structure)


  def test_all_valid_targets(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]

    expected_targets = [0, 3, 5, 6, 9, 12, 13, 14, 15]
    self.assertEqual(sorted(to_game(game_state).all_valid_targets('X')), expected_targets)
  
  # def test_all_valid_moves(self):
  #   game_state =               [['X', 'O', 'O', 'X', 'O'],
  #                               ['X', 'W', 'W', 'W', 'X'],
  #                               ['X', 'W', 'W', 'W', 'W'],
  #                               ['W', 'W', 'W', 'W', 'O'],
  #                               ['W', 'O', 'O', 'X', 'O']]
  #   expected_valid_moves = [(4, 0), (0, 4), (4, 3), (0, 4), (1, 0), (0, 4), (2, 0), (0, 4), (0, 3), (4, 0), (3, 4), (4, 0), (2, 4), (4, 0), (1, 4), (4, 0)]
  #   self.assertEqual(to_game(game_state).all_valid_moves('X'), expected_valid_moves)
    

  def test_should_move_row_true(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    self.assertTrue(to_game(game_state).should_move_row((0, 4)))

  def test_should_move_row_false(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    self.assertFalse(to_game(game_state).should_move_row((0, 12)))

  def test_should_move_row_from_left_true(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    self.assertTrue(to_game(game_state).should_move_row_from_left((4, 0)))

  def test_should_move_row_from_left_false(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    self.assertFalse(to_game(game_state).should_move_row_from_left((0, 4)))

  def test_should_move_column_from_top_true(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    self.assertTrue(to_game(game_state).should_move_column_from_top((12, 0)))

  def test_should_move_column_from_top_false(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    self.assertFalse(to_game(game_state).should_move_column_from_top((0, 12)))

  def test_apply_move(self):
    2

def to_simple_structure(game):
  return list(map(lambda row: list(map(lambda cell: cell.symbol_to_show(), row)), game.board))

def to_game(matrix):
  quixo = Quixo()
  for i_row in range(len(matrix)):
    for i_column in range(len(matrix[i_row])):
      cell = quixo.board[i_row][i_column]
      current_value = matrix[i_row][i_column]
      cell.update_symbol('empty' if current_value == 'W' else current_value)
  return quixo

if __name__ == '__main__':
  unittest.main()
