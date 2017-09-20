#
#   File: gyroscope.py
#   Author: Abraham Dick
#   Date Created: 09/19/2017
#   Description: Models a gyroscope
#

import numpy as np

class Gyroscope:

    __name = None
    __model = "Adafruit xxxxxx"
    __xyz_array = np.array([])

    def __init__(self,name):
        self.__name = name

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_model(self):
        return self.__model

    def get_xyz(self):
        return self.__xyz_array

    def add_data(self,xyz):
        np.append(self.__xyz_array,[xyz])


