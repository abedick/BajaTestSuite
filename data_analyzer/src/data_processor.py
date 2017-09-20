#
#   File: data_processor.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: In charge of processing the data from file
#

from src.terminal_driver import Driver

import os

class DataProcessor:
    __driver = None

    def __init__(self):
        self.__driver = Driver(100,"")
    
    def run(self):
        os.system("clear")
        self.__driver.title_print_ext("Data Processor","")

        get_data()

    def get_data(self):

        