from axelrod import player
from axelrod import tournament
turns=tournament.turns()

class TitForTatBrutus(Player):
    """A player starts by cooperating and then mimics previous move by opponent. 
    At the very last move, they defect"""

    name = 'Tit For Tat Brutus'

    def strategy(self, opponent):
        if len(opponent.history())==turns:
            return 'D'
        else:
            try:
                return opponent.history[-1]
            except IndexError:
                return 'C'
