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
        Helper method to initialize our City class object with rectangular coordinate data.

        INPUT(S):
            - x_pos {float}
            - y_pos {float}
        OUTPUT(S):
            N/A
        """
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __repr__(self):
        """
        Helper method to cleanly render self-contained coordinate data.

        INPUT(S):
            N/A
        OUTPUT(S):
            - {str}
        """
        return "({}, {})".format(str(self.x_pos), str(self.y_pos))

    def calculate_euclidean_distance(self, next_city):
        """
        Method to calculate distance between current and next city instances using Euclidean distance formula.

        INPUT(S):
            - next_city {City(object)}
        OUTPUT(S):
            - {float}
        """
        distance_x, distance_y = abs(self.x_pos - next_city.x_pos), abs(self.y_pos - next_city.y_pos)
        return np.sqrt((distance_x ** 2) + (distance_y ** 2))


####################################################################################################
########################################## MAIN RUN LOGIC ##########################################
####################################################################################################


def main():
    city_1, city_2 = City(0, 0), City(3, 4)
    dist_12 = city_1.calculate_euclidean_distance(city_2)
    return print("The distance between cities 1 and 2 is {} miles.".format(dist_12))

if __name__ == "__main__":
    main()