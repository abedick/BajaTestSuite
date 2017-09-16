#
#   File: controller.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: In charge of getting preliminary input from the user
#

from src.driver import Driver

class Controller:
    __driver = None

    def __init__(self,length):
        self.__driver = Driver(length,"")

    def run(self):
        self.__driver.title_print_ext("Data Analyzer for Baja","Make a selection")
