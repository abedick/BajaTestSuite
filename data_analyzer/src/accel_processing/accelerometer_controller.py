#
#   File: main.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description:
#


from src.driver import Driver
from src.drivers.csv_reader import CSV_reader
from src.accel_processing.accelerometer import Accelerometer

import os

class AccelerometerController:
    __main_title = "Design Review 2 Test Mode"

    __driver = None
    __csv_read = None

    __filename = None

    __number_accel = None
    __accel_array = []

    def __init__(self):
        self.__driver = Driver(100,"")

    def run(self):
        # start the frame
        os.system("clear")
        self.__driver.title_print_ext(self.__main_title,"Make a selection")

        # Aquire the filename and get the reader environment setup
        self.__get_filename()
        self.__csv_read.setup()

        # aquire information about the datafile
        self.__get_data()

        # create the array of accelerometers
        for i in range(0,self.__number_accel):
            new_accel = self.__create_accelerometers(i+1)
            self.__accel_array.append(new_accel)

    # gets a valid filename from the user
    def __get_filename(self):
        os.system("clear")
        self.__driver.title_print_ext(self.__main_title,"Get a filename")

        print("\n{}Data files are typically stored in the data folder".format(self.__driver.spacer()))
        print("{}Data files must be stored in the csv file format".format(self.__driver.spacer()))
        print("{}Filenames are typically the date and trial number associated with the data that was collected\n".format(self.__driver.spacer()))

        # filename = input("{}Enter a filename: ".format(self.__driver.spacer()))

        filename = "09_16_2017.txt"
        filepath = "./data/"

        self.__csv_read = CSV_reader(filename,filepath)
    
    # gets data line for line from the CSV reader
    def __get_data(self):

        # Get data to construct the accelerometer objects
        self.__number_accel = self.__csv_read.get_next()
        self.__number_accel = int(self.__number_accel)

        print("{}{} accelerometer(s) detected".format(self.__driver.spacer(),self.__number_accel))

    def __create_accelerometers(self,number):
        #name,position

        accel_name = input("\n{}Enter a name for accelerometer {}: ".format(self.__driver.spacer(),number))
        accel_position = input("{}Enter a position for accelerometer {}: ".format(self.__driver.spacer(),number))
        temp_accel = Accelerometer(accel_name,accel_position,[],[],[])
        
        return temp_accel