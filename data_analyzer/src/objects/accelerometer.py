#
#   File: accelerometer.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: Models a 3 axis accelerometer using arrays to hold the x, y, and z axis
#

import numpy as np

class Accelerometer:

    __name = None
    __model = "Adafruit MMA8451"
    __position = None
    __xyz_array = None
    __number_datapoints = None

    def __init__(self,name,position,number_points):
        self.__name = name
        self.__position = position
        self.__number_datapoints = number_points
        self.__xyz_array = np.empty([number_points,3])

    def set_name(self,name):
        self.__name = name
    
    def set_position(self,position):
        self.__position = position

    def get_name(self):
        return self.__name
    
    def get_position(self):
        return self.__position

    def get_model(self):
        return self.__model

    def get_xyz(self):
        return self.__xyz_array

    def add_data(self,xyz,row):
        self.__xyz_array = np.append(self.__xyz_array,xyz)


