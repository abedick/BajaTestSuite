#
#   File: csv_reader.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description:
#

from src.accel_processing.accelerometer import Accelerometer

class CSV_reader:
    __filename = None
    __path_to_file = None
    __filename_path = None
    __Accelerometer_array = []

    __number_accel = None
    __open_file = None


    def __init__(self,filename,path):
        self.__filename = filename
        self.__path_to_file = path
        self.__filename_path = path + filename

    def setup(self):
        self.__check_file()

    def __check_file(self):
        self.__filename_path = self.__path_to_file + self.__filename
        self.__open_file = open(self.__filename_path,'r')

    def get_next(self):
        return self.__open_file.readline().rstrip('\n')