# Handles all backend computations for the game, including time limits, countering, 
# managing turns, storing a record of all plays in order, and determining 
# whether a player has won yet.

import requests # this will be needed to handle HTTP GET requests

Queue moves # this will store all the moves in order

int player # keeps track of whose turn it is

int timeUntilTurnSwitch # keeps track of how much time is left
                        # until the current turn ends

int turnLength # how long each turn is

bool[] survivingPlayers # keeps track of which players are still alive

def startTurnTimer(allPlayers, turnLength):
    '''
    When called, makes it allPlayers[0]’s turn and starts and
    manages a turn timer.

    allPlayers: a string list of all players
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

def elimPlayer(player): 
    '''
    Runs any graphical functions that will be called upon a
    player being out, and sets survivingPlayers[player] to
    false.

    player: an integer representing the player

    returns: True on success, False on failure
    '''

def counter(counter):
    '''
    Appends counter to 
    '''
