from quixo_fede import Quixo

class QuixoPlayer:
  def __init__(self):
    self.game = Quixo()
  
  def playerPlay(self):
    # Missing implementation
    None

  def oponentPlay(self, oponent, move):
    self.game.apply_move(oponent, move)
