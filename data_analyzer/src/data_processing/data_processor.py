#
#   File: controller.py
#   Author: Abraham Dick
#   Date Created: 09/19/2017
#   Description: In charge of processing data
#

from src.driver import Driver
from src.dataset import Dataset
from src.accel_processing.accelerometer import Accelerometer

import matplotlib.pyplot as plt
import numpy as np

import os

class DataProcessor:
    __driver = None
    __dataset = None

    def __init__(self, raw_data):
        self.__dataset = raw_data
        self.__driver = Driver(100,"")

    def run(self):
        os.system("clear")
        self.__driver.title_print_ext("Data Processing","Create Report")

        print("{} name".format(self.__dataset.get_name()))

        accel_data = self.__dataset.get_accel_array()

        

        # plottable_data = np.array(accel_data[0].get_x(),accel_data[0].get_y())

        x = range(0,len(accel_data.get_x()))

        plt.plot(x,accel_data.get_x())
        plt.ylabel('Force (m/s^2)')
        plt.xlabel('Time Passing')
        plt.show()

    def grapher(self):
        print("dummy text")