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
    __x_dir = None
    __y_dir = None
    __z_dir = None

    def __init__(self,name,position,x,y,z):
        self.__name = name
        self.__position = position
        self.__x_dir = x
        self.__y_dir = y
        self.__z_dir = z

    def get_x:
        return self.__x_dir

    def get_y:
        return self.__y_dir

    def get_z:
        return self.__z_dir
