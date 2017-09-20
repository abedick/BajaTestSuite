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
 
        accel1 = __accelerometer_array[0].get_xyz()
        accel2 = __accelerometer_array[1].get_xyz()
        accel3 = __accelerometer_array[2].get_xyz()
        accel4 = __accelerometer_array[3].get_xyz()
        accel5 = __accelerometer_array[4].get_xyz()
        accel6 = __accelerometer_array[5].get_xyz()

        daccel1x = []
        daccel1y = []
        daccel1z = []


                # print(accel1[0][0])

        for i in range(0,len(accel2)):
            daccel1x.append(accel1[i][0])
            daccel1y.append(accel2[i][1])
            daccel1z.append(accel3[i][2])


        # print(temp_arr)

        # y = [range(0,__number_data_points)]
        a1 = daccel1x
        a2 = daccel1y
        a3 = daccel1z


        plt.plot(a1, label='accel1', linestyle='solid', color='blue')
        plt.plot(a2, label='accel2', linestyle='solid', color='orange')
        plt.plot(a3, label='accel3', linestyle='solid', color='black')
        plt.legend()
        plt.show()


        # # print(accel1[0][0])

        # for i in range(0,len(accel2)):
        #     daccel1.append(accel1[i][0])
        #     daccel2.append(accel2[i][0])
        #     daccel3.append(accel3[i][0])
        #     daccel4.append(accel4[i][0])
        #     daccel5.append(accel5[i][0])
        #     daccel6.append(accel6[i][0])

        # # print(temp_arr)

        # # y = [range(0,__number_data_points)]
        # a1 = daccel1
        # a2 = daccel2
        # a3 = daccel3
        # a4 = daccel4
        # a5 = daccel5
        # a6 = daccel6

        # plt.plot(a1, label='accel1', linestyle='solid', color='blue')
        # plt.plot(a2, label='accel2', linestyle='solid', color='orange')
        # plt.plot(a3, label='accel3', linestyle='solid', color='black')
        # plt.plot(a4, label='accel4', linestyle='solid', color='yellow')
        # plt.plot(a5, label='accel5', linestyle='solid', color='green')
        # plt.plot(a6, label='accel6', linestyle='solid', color='brown')
        # plt.legend()
        # plt.show()



''' Map

            data[i][0]
'''