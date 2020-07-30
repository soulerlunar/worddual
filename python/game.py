# The game object used for games of Word Dual.

class Game:
    '''
    An object used to track the players, current turn, and turn length
    within a game of Word Dual.
    '''

    def __init__(self, players, turn_length):
        self.players = players # a string list of players in a game
        self.current_player = -1 # int for current player's turn. -1 means none
        self.turn_length = turn_length # int length in seconds of each turn

    def elimPlayer(player): 
        '''
        Runs any graphical functions that will be called upon a
        player being out, and removes player from self.players[].

        player: an integer representing the player

        returns: True on success, False on failure
        '''

    def incrementTurn():
        '''
        Increases the value of current_player by one

        returns: Always true
        '''