from axelrod import player
from axelrod import tournament
turns=tournament.turns()

class TitForTatQuickShot(Player):
    """A player starts by cooperating and then mimics previous move by opponent. 
    On the first move, they sneak a quick defection and then act normally"""

    name = 'Tit For Tat Quick Shot'

    def strategy(self, opponent):
        if len(opponent.history())==0:
            return 'D'
        else:
            try:
                return opponent.history[-1]
            except IndexError:
                return 'C'