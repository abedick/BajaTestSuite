#
#   File: controller.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: In charge of getting preliminary input from the user
#

from src.driver import Driver
from src.dataset import Dataset
from src.accel_processing.accelerometer_controller import AccelerometerController
from src.data_processing.data_processor import DataProcessor

import os

class Controller:
    __driver = None
    __dataset = None
    __processed_raw_data = None

    def __init__(self,length):
        self.__driver = Driver(length,"")

    def run(self):
        self.__driver.title_print_ext("Data Analyzer for Baja","Make a selection")

        options = ["Accelerometer Data Analysis",
                   "Design Review 2 Test Mode",
                   "Quit"]

        choice = self.__driver.mbcg(options)

        if(choice == 1):
            pass
        elif(choice == 2):
            self.__create_dataset()
            accel_control = AccelerometerController(self.__dataset)
            self.__processed_raw_data = accel_control.run()

            data_process = DataProcessor(self.__processed_raw_data)
            data_process.run()


        else:
            pass

    def __create_dataset(self):
        os.system("clear")
        self.__driver.title_print_ext("Accelerometer Processing","Create a dataset")

        name = input("{}Name for Dataset: ".format(self.__driver.spacer()))
        date = input("{}Date data was recorded: ".format(self.__driver.spacer()))
        user = input("{}User Name for Dataset: ".format(self.__driver.spacer()))

        self.__dataset = Dataset(name,date,user)