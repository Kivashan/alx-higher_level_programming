#!/usr/bin/python3
import sys

class Queen:
    '''Class defining the Queen chess piece'''
    
    queen_instances = 0

    def __init__(self, col, row):
        '''Initialization method for a Queen object'''
        self.row = row
        self.col = col
        Queen.queen_instances += 1

    def __del__(self):
        '''Destroy queen instances'''
        Queen.queen_instances -= 1

    @staticmethod
    def check_col(queen_1, queen_2):
        '''Method that checks if two queens occupy the same column

        Args:
            queen_1: Instance of Queen class
            queen_2: Instance of Queen class

        Return:
            Returns True if queens occupy same col, False otherwise
        '''
        if queen_1.col == queen_2.col:
            return True
        return False

    def check_row(queen_1, queen_2):
        '''Method that checks if two queens occupy the same row

        Args:
            queen_1: Instance of the Queen class
            queen_2: Instance of the Queen class

        Return:
            Returns True if queens occupy the same row, False otherwise
        '''
        if queen_1.row == queen_2.row:
            





if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
    else:
        print("Howdy")
