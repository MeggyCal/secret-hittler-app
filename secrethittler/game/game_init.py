from numpy import random
import constants

class Lotery:
    """ Assigns roles to players.
    We know that the number of players is valid."""
    def __init__(self, n):
        self.n = n
        self.roles = numpy.random.permutation(self.n)

    def assign(self, players):
        l, f = constants.roles[self.n]
        # there should be one Hittler
        assert(l + f = self.n - 1)
        for i in range(self.roles):
            if (self.roles[i] < liberal):
                players[i].party = "liberal"
                players[i].id = "liberal"
            else if (self.roles[i] < l + f):
                players[i].party = "fascist"
                players[i].id = "fascist"
            else:
                players[i].party = "fascist"
                players[i].id = "Hittler"


class GameBoard:
    """ The game board which will be used during the game. """
    def __init__(self, n):
    """ Constructs an initial game board. """

        self.n = n

        self.laws_agreed = {
            l = 0,
            f = 0
        }

        self.laws_l = constants.laws_l
        self.laws_f = constants.laws_f
        self.laws_available = constants.laws_l + constants.laws_f
        self.laws_discarded_l = 0
        self.laws_discarded_f = 0

        self.specials = constants.f_specials[n]

        self.president = None
        self.prev_president = None
        self.chancelor = None
        self.prev_chancelor = None
        
        self.check_chancelor = False

    def take_three_laws(self):
        """ Chooses three laws at random. """
        laws = ()
        for i in range(3):
            if(self.laws_available == 0):
                self.refresh_laws()
            law = numpy.random.randint(self.laws_available--)
            if(law < self.laws_l):
                self.laws_l--
                laws.append(True)
            else:
                self.laws_f--
                laws.append(False)

        return laws

    def refresh_laws(self):
        self.laws_l = self.laws_discarded_l
        self.laws_f = self.laws_discarded_f
        self.laws_discarded_l = 0
        self.laws_discarded_f = 0
        self.laws_available = self.laws_l + self.laws_f


