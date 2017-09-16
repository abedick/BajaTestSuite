#
#   File: csv_reader.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: Reader specifically used to process data from the csv file from Arduino output
#

from src.accel_processing.accelerometer import Accelerometer
import csv

class CSV_reader:
    __filename = None
    __path_to_file = None
    __filename_path = None
    __Accelerometer_array = []

    __number_accel = None
    __open_file = None

    __read_in_data = None

    __x_values = []
    __y_values = []
    __z_values = []


    def __init__(self,filename,path):
        self.__filename = filename
        self.__path_to_file = path
        self.__filename_path = path + filename

    def setup(self):
        self.__check_file()

    def __check_file(self):

        with open(self.__filename_path, newline='') as csvfile:
            self.__read_in_data = csv.reader(csvfile,delimiter=',')

            # self.__number_accel = self.__read_in_data.next()

            for row in self.__read_in_data:
                print(row)

            
        # print("{}".format(self.__number_accel)

    def get_information(self):
    #     # self.__number_accel = self.__read_in_data[0]
        return self.__number_accel

    # def __read_data(self):


    def get_data(self):
        with open(self.__filename_path, newline='') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            
            for row in readCSV:

                x_val = row[1]
                y_val = row[2]
                z_val = row[3]

                self.__x_values.append(x_val)
                self.__y_values.append(y_val)
                self.__z_values.append(z_val)
        
    def return_data(self):

        accel_1_list = [self.__x_values,self.__y_values,self.__z_values]
        return(accel_1_list)