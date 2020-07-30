# Handles all backend computations for the game, including time limits, countering, 
# managing turns, storing a record of all plays in order, and determining 
# whether a player has won yet.

import requests # this will be needed to handle HTTP GET requests

Queue moves # this will store all the moves in order

int timeUntilTurnSwitch # keeps track of how much time is left
                        # until the current turn ends

def startTurnTimer(game):
    '''
    When called, makes it allPlayers[0]’s turn and starts and
    manages a turn timer.

    game: a game object
    turnLength: an int representing the turn length in seconds

    returns: None
    '''

def endTurn():
    '''
    Ends the current player’s turn, incrementing player by 1 mod
    len(allPlayers), resetting counters, and resetting 
    timeUntilTurnSwitch to turnLength

    returns: None
    '''

def makePlay(play):
    '''
    Checks whether this play has been countered; if it has been,
    calls elimPlayer(player). Otherwise, it appends play to
    moves and calls endTurn().

    play: a string containing the phrase the player played

    return: True if play is not counter, False if the play was 
    countered and fails
    '''