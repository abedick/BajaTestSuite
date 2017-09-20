#
#   File: csv_reader.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: Reader specifically used to process data from the csv file from Arduino output
#

from src.accel_processing.accelerometer import Accelerometer
import csv

import numpy as np

class CSV_reader:
    __filename = None
    __path_to_file = None
    __filename_path = None
    __Accelerometer_array = []

    __number_accel = None
    __open_file = None

    __read_in_data = None

    __reading = []


    def __init__(self,filename,path):
        self.__filename = filename
        self.__path_to_file = path
        self.__filename_path = path + filename

        # for i in range(0,18):
        #     self.__reading[i] = []

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

                self.__reading[0].append(row[0])
                self.__reading[1].append(row[1])
                self.__reading[2].append(row[2])
                self.__reading[3].append(row[3])
                self.__reading[4].append(row[4])
                self.__reading[5].append(row[5])
                self.__reading[6].append(row[6])
                self.__reading[7].append(row[7])
                self.__reading[8].append(row[8])
                self.__reading[9].append(row[9])
                self.__reading[10].append(row[10])
                self.__reading[11].append(row[11])
                self.__reading[12].append(row[12])
                self.__reading[13].append(row[13])
                self.__reading[14].append(row[14])
                self.__reading[15].append(row[15])
                self.__reading[16].append(row[16])
                self.__reading[17].append(row[17])
                self.__reading[18].append(row[18])


        
    def return_data(self):

        return(self.__reading)