"""
FILENAME:       main.py
PROJECT:        Evolution of a Salesman.
AUTHOR:         Aakash "Kash" Sudhakar
DESCRIPTION:    Python project using genetic algorithms to approximate a solution to 
                the NP-Hard Traveling Salesman problem.
"""


####################################################################################################
############################ IMPORT STATEMENTS AND GLOBAL DECLARATIONS #############################
####################################################################################################


import numpy as np
import pandas as pd
import random as rand
import operator as op
import matplotlib.pyplot as plt


####################################################################################################
####################################### OBJECT ARCHITECTURES #######################################
####################################################################################################

class City(object):
    """ Object architecture that contains structural logic for our city representation. """
    def __init__(self, x_pos, y_pos):
        """
        Initializing our City class object with rectangular coordinate data.

        INPUT(S):
            - x_pos {float}
            - y_pos {float}
        OUTPUT(S):
            N/A
        """
        self.x_pos = x_pos
        self.y_pos = y_pos