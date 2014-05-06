#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random

class NQueens:
    'This class is used to create a nxn chessboard and ' \
        '"evolve" a non-conflicting solution of Queen Placements'

    # Initializes a board with n Queens in random positions
    def __init__(self, queen_count=0):
        self.queen_count = queen_count
        
    def random_set_up(self):
        self.board = []

    def set_position_key(self):
        random_key = random.SystemRandom()
        position_key = random_key.randint(10 ** self.queen_count)

    #Returns the position of the queen in the given column
    def get_position(self, column=0):
        print "Getting Queen position at column %d" % (column)
        pass #ZZZ
        
        

    

    
    
