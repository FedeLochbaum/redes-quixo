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

  def test_valid_moves_for_cell_1(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    game = to_game(game_state)
    self.assertEqual(sorted(game.valid_moves_for_cell(game.board[0][0])), [(0, 4), (0, 12)])

  def test_valid_moves_for_cell_2(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    game = to_game(game_state)
    self.assertEqual(sorted(game.valid_moves_for_cell(game.board[0][2])), [(2, 0), (2, 4), (2, 10)])
  
  def test_all_valid_moves(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    expected_valid_moves = [(0, 4), (0, 12), (3, 4), (3, 0), (3, 9), (5, 15), (5, 4), (5, 8), (6, 14), (6, 4), (6, 8), (9, 8), (9, 12), (9, 3), (12, 8), (12, 0), (13, 7), (13, 0), (13, 12), (14, 6), (14, 0), (14, 12), (15, 5), (15, 0), (15, 12)]
    self.assertEqual(to_game(game_state).all_valid_moves('X'), expected_valid_moves)

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

  def test_apply_move_a_row_from_left(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]

    expected_game =            [['O', 'O', 'X', 'O', 'X'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    game = to_game(game_state)
    game.apply_move('X', (0, 4))
    self.assertEqual(to_simple_structure(game), expected_game)

  def test_apply_move_a_row_from_right(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]

    expected_game =            [['O', 'X', 'O', 'O', 'X'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    game = to_game(game_state)
    game.apply_move('O', (4, 0))
    self.assertEqual(to_simple_structure(game), expected_game)

  def test_apply_move_a_colum_from_top(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]

    expected_game =            [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['W', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['X', 'O', 'O', 'X', 'O']]
    game = to_game(game_state)
    game.apply_move('X', (0, 12))
    self.assertEqual(to_simple_structure(game), expected_game)

  def test_apply_move_a_colum_from_bottom(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['X', 'O', 'O', 'X', 'O']]

    expected_game =            [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['X', 'W', 'W', 'W', 'O'],
                                ['W', 'O', 'O', 'X', 'O']]
    game = to_game(game_state)
    game.apply_move('X', (12, 0))
    self.assertEqual(to_simple_structure(game), expected_game)

  def test_is_game_over_false(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['W', 'W', 'W', 'W', 'O'],
                                ['X', 'O', 'O', 'X', 'O']]

    self.assertFalse(to_game(game_state).is_game_over((0, 0), 'X'))

  def test_is_game_over_true_veritcal(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'W', 'W', 'W', 'X'],
                                ['X', 'W', 'W', 'W', 'W'],
                                ['X', 'W', 'W', 'W', 'O'],
                                ['X', 'O', 'O', 'X', 'O']]

    self.assertTrue(to_game(game_state).is_game_over((0, 0), 'X'))

  def test_is_game_over_true_diagonal(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'X', 'W', 'W', 'X'],
                                ['X', 'W', 'X', 'W', 'W'],
                                ['O', 'W', 'W', 'X', 'O'],
                                ['X', 'O', 'O', 'X', 'X']]

    self.assertTrue(to_game(game_state).is_game_over((0, 0), 'X'))

  def test_is_game_over_true_horizontal(self):
    game_state =               [['X', 'O', 'O', 'X', 'O'],
                                ['X', 'O', 'W', 'W', 'X'],
                                ['X', 'X', 'X', 'X', 'X'],
                                ['O', 'W', 'W', 'X', 'O'],
                                ['X', 'O', 'O', 'X', 'X']]

    self.assertTrue(to_game(game_state).is_game_over((2, 0), 'X'))

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
