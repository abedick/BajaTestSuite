#
#   File: main.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description:
#
from src.driver import Driver

import os

class AccelerometerController:
    __driver = None

    def __init__(self):
        self.__driver = Driver(100,"")

    def run(self):
        os.system("clear")
        self.__driver.title_print_ext("Design Review 2 Test Mode","Make a selection")

