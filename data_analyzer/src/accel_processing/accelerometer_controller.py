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
    __main_title = "Design Review 2 Test Mode"
    __filename_aquired = False
    __filename = None

    def __init__(self):
        self.__driver = Driver(100,"")

    def run(self):
        if not(self.__filename_aquired):
            self.__get_filename()

        # os.system("clear")
        # self.__driver.title_print_ext(self.__main_title,"Make a selection")

    # gets a valid filename from the user
    def __get_filename(self):
        os.system("clear")
        self.__driver.title_print_ext(self.__main_title,"Get a filename")

        print("\n{}Data files are typically stored in the data folder".format(self.__driver.spacer()))
        print("{}Data files must be stored in the csv file format".format(self.__driver.spacer()))
        print("{}Filenames are typically the date and trial number associated with the data that was collected\n".format(self.__driver.spacer()))

        filename = input("{}Enter a filename: ".format(self.__driver.spacer()))

        filepath = "../../data/" +  filename

        print(filepath)

