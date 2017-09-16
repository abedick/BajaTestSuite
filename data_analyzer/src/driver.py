#
#   File: driver.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   
#   Description: In charge of printing to terminal

import sys

class Driver :

    __line_length = 50
    __version = None

    def __init__(self,length,version) :
        self.__line_length = length
        self.__version = version

    def spacer(self):
        return("      ")

    def logo_print(self) :
        print("""   __              _                    _                   _                                  _
   \ \  __ _ _   _| |__   __ ___      _| | __   /\/\   ___ | |_ ___  _ __ ___ _ __   ___  _ __| |_ ___
    \ \/ _` | | | | '_ \ / _` \ \ /\ / / |/ /  /    \ / _ \| __/ _ \| '__/ __| '_ \ / _ \| '__| __/ __|
 /\_/ / (_| | |_| | | | | (_| |\ V  V /|   <  / /\/\ \ (_) | || (_) | |  \__ \ |_) | (_) | |  | |_\__ \ 
 \___/ \__,_|\__, |_| |_|\__,_| \_/\_/ |_|\_\ \/    \/\___/ \__\___/|_|  |___/ .__/ \___/|_|   \__|___/ 
              |___/                                                           |_|""")

        print("\nDeveloped by Abe Dick, Version",self.__version)

    def title_print(self,title):
        title_size = len(title)

        # top line
        print("\n\u250C", end='')
        for i in range(0,self.__line_length):
            print("\u2500", end='')
        print("\u2510")

        # title line
        print("\u2502 \u25B6",title,end='')
        for i in range(self.__line_length-7-title_size):

            if i == ((self.__line_length-title_size)-9):
                print("[JMS]",end='')
            else :
                print(" ",end='')
        print("\u2502")

        # bottom line
        print("\u2514",end='')
        for i in range(self.__line_length):
            print("\u2500",end='')
        print("\u2518")
    
    def title_print_ext(self,title,sub):
        title_size = len(title)

        # top line
        print("\n\u250C", end='')
        for i in range(self.__line_length):
            print("\u2500", end='')
        print("\u2510")

        # title line
        print("\u2502 \u25B6",title,end='')
        for i in range(self.__line_length-7-title_size):

            if i == ((self.__line_length-title_size)-9):
                print("[JMS]",end='')
            else :
                print(" ",end='')
        print("\u2502")

        # middle line
        print("\u2514",end='')

        for i in range(0,self.__line_length):
            if i == 3:
                print("\u252C",end='')
            else:
                print("\u2500",end='')
        print("\u2534\u2500\u2500\u2500\u2510")

        # sub title line

        sub_size = len(sub)
        print("    \u2502 \u25B6 ",sub,end='')
        for i in range(self.__line_length - (sub_size+4)):
            if i == (self.__line_length-7 - sub_size):
                print("\u2517",end='')
            else:
                print(' ',end='')
        print("\u2502")

        # bottom line
        print("    \u2514",end='')
        for i in range(self.__line_length):
            print("\u2500",end='')
        print("\u2518")
    
    def mbcg(self,option_list):
        self.menu_builder(option_list)
        choice = self.choice_validation(1,len(option_list))
        return choice

    def menu_builder(self,option_list):
        for i in range(len(option_list)):
            print("{}{}. {}".format(self.spacer(),i+1,option_list[i]))
    
    def choice_validation(self,low,high):
        choice = 0
        print("{}--------------------".format(self.spacer()))
        while (choice < low or choice > high):
            while True:
                try:
                    choice = int(input("{}Choice: ".format(self.spacer())))
                except ValueError:
                    print("{}Please enter a number".format(self.spacer()))
                    continue
                else:
                    break

        return choice