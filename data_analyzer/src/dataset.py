#
#   File: dataset.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: Models a dataset
#

class Dataset:

    __name = None
    __date = None
    __user = None
    __accel_array = []
    __gyro = None

    def __init__(self,name,date,user):
        self.__name = name
        self.__date = date
        self.__user = user
    
    def set_accel_array(self, array):
        self.__accel_array = array

    def set_gyro(self, array):
        self.__gyro = array

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_user(self):
        return self.__user

    def get_accel_array(self):
        return self.__accel_array

    def get_gyro(self):
        return self.__gyro
