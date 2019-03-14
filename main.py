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
        Initializer (helper) method to fill our City class object with rectangular coordinate data.

        INPUT(S):
            - x_pos {float}
            - y_pos {float}
        OUTPUT(S):
            N/A
        """
        self.x_pos, self.y_pos = x_pos, y_pos

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


class Fitness(object):
    """ Incomplete object. """
    def __init__(self, path):
        """ 
        Initializer (helper) method to set our path (route), distance, and fitness score values 
        upon object declaration. 

        INPUT(S):
            - path {list(int)}
        OUTPUT(S):
            N/A
        """
        self.path = path
        self.distance = int(0)
        self.fitness = float(0.0)

    def path_distance(self):
        """ 
        Method to approximate overall path metric based on iterated walk across random city array. 
        
        INPUT(S):
            N/A
        OUTPUT(S):
            Fitness().distance {int}
        """
        if self.distance == 0:
            distance_path = 0

            # Creates discrete path graph from matrix of city values
            for iterator in range(len(self.path)):
                current_city, next_city = self.path[iterator + 1], None
                if iterator + 1 < len(self.path):
                    next_city = self.path[iterator + 1]
                else:
                    next_city = self.path[0]

                # Iteratively adds distance values to overall path distance measure
                distance_path += current_city.calculate_euclidean_distance(next_city)
            self.distance = distance_path
        return self.distance

    def path_fitness(self):
        """ 
        Method to approximate path fitness score as inverse of path distance calculation. 
        
        INPUT(S):
            - N/A
        OUTPUT(S):
            - Fitness().fitness {float}
        """
        if self.fitness == 0:
            self.fitness = 1 / float(self.path_distance())
        return self.fitness


####################################################################################################
########################################## MAIN RUN LOGIC ##########################################
####################################################################################################


def main():
    city_1, city_2 = City(0, 0), City(3, 4)
    dist_12 = city_1.calculate_euclidean_distance(city_2)
    return print("The distance between cities 1 and 2 is {} miles.".format(dist_12))

if __name__ == "__main__":
    main()