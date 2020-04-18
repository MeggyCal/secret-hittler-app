""" Constants given by the rules. """
# please, correct me, I am lazy to look into the rules
constants = {
    """ Number of liberals and fascists depending on the number of players.
    Corresponds to 'players: (liberals, fascists)'. """
    roles = {
        5: (3, 1),
        6: (3, 2)
        # TODO
    }


    """ Actions which happen when a fascist law is agreed. """
    f_specials = {
        5: (None, None, "search", "kill", "kill") # here will be function pointers or something
        # TODO
    }

    """ Number of laws in the pack. """
    laws_l = 6
    laws_f = 12
}

