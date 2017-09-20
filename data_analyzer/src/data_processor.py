#
#   File: data_processor.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: In charge of processing the data from file
#

from src.terminal_driver import Driver
from src.objects.dataset import Dataset 
from src.objects.accelerometer import Accelerometer
from src.objects.gyroscope import Gyroscope

import os
import _ctypes
import numpy as np
from io import BytesIO
from numpy import genfromtxt

import matplotlib.pyplot as plt

class DataProcessor:
    __driver = None
    __filename = './data/09/18/2017.csv'
    __data = None
    __dataset = None

    def __init__(self):
        self.__driver = Driver(100,"")
    
    def run(self):
        os.system("clear")
        self.__driver.title_print_ext("Data Processor","")

        self.__get_data()
        self.__create_objects()

    def __get_data(self):
        self.__data = np.genfromtxt('./data/09_19_2017.csv', delimiter=',')

    def __create_objects(self):
        __number_data_points = len(self.__data)
        __number_cols = len(self.__data[0])
        __number_accel = __number_cols // 3

        print("{}{} datapoints taken from {} Accelerometers and 1 Gyroscope".format(self.__driver.spacer(),__number_data_points,__number_accel))
        print("{}Processing data".format(self.__driver.spacer()))

        __accelerometer_array = []

        # Create the correct number of accelerometers
        for i in range(__number_accel):
            new_accelerometer = Accelerometer(i,"",__number_data_points)
            __accelerometer_array.append(new_accelerometer)

        # Create the gyroscope
        __gyroscope = Gyroscope("Gyro")

        # Take the data table and put things in their correct places

        for i in range(0,__number_data_points):

            # Add to the groscope
            __gyroscope.add_data([self.__data[i][0]])

            # Add each accelerometer

            for k in range(0,__number_accel):
                xyz_list = None
                __x_val = k*3+1
                __y_val = k*3+2
                __z_val = k*3+3

                xyz_list = [self.__data[i][__x_val],self.__data[i][__y_val],self.__data[i][__z_val]]

                # print(xyz_list)

                __accelerometer_array[k].add_data(xyz_list,k)

            # row = self.__data[i]
            # print(row)

        print("done")


        np.set_printoptions(suppress=True)   
        test = __accelerometer_array[0].get_xyz()

        print(type(test))
        print(test)
        print(np.prod(test.shape))
        print(test.ndim)

        # x = range(0,__number_data_points)

        # plt.plot(x)
        # plt.ylabel('Force (m/s^2)')
        # plt.xlabel('Time Passing')
        # plt.show()




''' Map

            data[i][0]
'''