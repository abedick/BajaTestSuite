#
#   File: accelerometer.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: Models a 3 axis accelerometer using arrays to hold the x, y, and z axis
#

class Accelerometer:

    __name = None
    __model = "Adafruit MMA8451"
    __position = None
    __x_dir = []
    __y_dir = []
    __z_dir = []

    def __init__(self,name,position,x,y,z):
        self.__name = name
        self.__position = position
        self.__x_dir = x
        self.__y_dir = y
        self.__z_dir = z

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

    def get_x(self):
        return self.__x_dir

    def get_y(self):
        return self.__y_dir

    def get_z(self):
        return self.__z_dir

    def add_to_x(self,x_value):
        self.__x_dir.append(x_value)

    def add_to_y(self,y_value):
        self.__y_dir.append(y_value)

    def add_to_z(self,z_value):
        self.__z_dir.append(z_value)
