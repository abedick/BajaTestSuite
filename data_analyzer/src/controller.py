#
#   File: controller.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: In charge of getting preliminary input from the user
#

from src.driver import Driver
from src.accel_processing.accelerometer_controller import AccelerometerController

class Controller:
    __driver = None

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
            accel_control = AccelerometerController()
            accel_control.run()
        else:
            pass