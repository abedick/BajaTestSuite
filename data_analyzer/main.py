#
#   File: main.py
#   Author: Abraham Dick
#   Date Created: 09/16/2017
#   Description: In charge of setting up data aquisition program and printing the application logo
#

from src.driver import Driver

import os

# Version Information
version = "Alpha 0.00.034"

def main():
    drive = Driver(100,version)

    os.system("clear")
    drive.logo_print()

    drive.title_print_ext("Data Analyzer for Baja","Make a selection")



main()