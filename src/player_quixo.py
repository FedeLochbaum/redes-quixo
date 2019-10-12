from quixo_fede import Quixo
from copy import deepcopy
from  alpha_beta import alphabeta

class QuixoPlayer:
  def __init__(self):
    self.game = Quixo()
    self.player = None
  
  def set_player(self, player):
    self.player = player
  
  def playerPlay(self):
    if self.player == None: self.set_player('X')
    move = self.next_move_using_iterative_deepening()
    self.game.apply_move(self.player, move)
    return move

  def oponentPlay(self, oponent, move):
    if self.player == None: self.set_player('O')
    self.game.apply_move(oponent, move)

  def next_move_using_iterative_deepening(self):
    # Missing implementation
    return alphabeta(deepcopy(self.game), 2, self.alpha, self.beta, self.player, h)