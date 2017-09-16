#
#   File: driver.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   
#   Description: In charge of printing to terminal

class Driver :

    __line_length = 50

    def __init__(self,length) :
        self.__line_length = length

    def logo_print(self) :
        print("""   __              _                    _                   _                                  _
   \ \  __ _ _   _| |__   __ ___      _| | __   /\/\   ___ | |_ ___  _ __ ___ _ __   ___  _ __| |_ ___
    \ \/ _` | | | | '_ \ / _` \ \ /\ / / |/ /  /    \ / _ \| __/ _ \| '__/ __| '_ \ / _ \| '__| __/ __|
 /\_/ / (_| | |_| | | | | (_| |\ V  V /|   <  / /\/\ \ (_) | || (_) | |  \__ \ |_) | (_) | |  | |_\__ \ 
 \___/ \__,_|\__, |_| |_|\__,_| \_/\_/ |_|\_\ \/    \/\___/ \__\___/|_|  |___/ .__/ \___/|_|   \__|___/ 
              |___/                                                           |_|""")

