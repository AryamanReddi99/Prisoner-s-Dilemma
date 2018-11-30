from axelrod import Player

class AntiAppeaser(Player):
    """A player who alternates when the opponent is satisfied - in effect, a corollary to the appeaser class
    """

    name = 'AntiAppeaser'

    def strategy(self, opponent):
        if len(self.history) == 0:
            self.str = 'C'
        else:
            if opponent.history[-1] == 'C':
                if self.str == 'C':
                    self.str = 'D'
                else:
                    self.str = 'C'
        return self.str

