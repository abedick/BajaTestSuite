import random
import sys
import os


# # basic

# '''
# print ('Hello World')
# '''

# # comments use hash

# #has to start with a letter
# name = "Abe"

# print(name)

# # main types
# # Numbers, Strings, lists, Tuples, Dictionaries

# # Operators + - * / % ** (exponentional) // (floor division, discard remainder)

# # to keep from using new lines
# print("Test",end="")
# print(" newlines")

# multiline_quote = ''' testing this out

# right now'''

# print (multiline_quote)

# # print("%s %s %s" % ('test'),name,multiline_quote)

# # lists 
# grocery_list = ['juice','tomatoes','15']
# print("first item ", grocery_list[0])

# print(grocery_list[1:3])

# other_things = ['wash','kids','check']
# to_do = [other_things,grocery_list]

# print(to_do)

# grocery_list.append('onions')
# print(to_do)
# grocery_list.sort()
# print(grocery_list)

# # length len(list_name)
# # max max(list_name)
# # min min(list_name)

# # Tuples

# pi_tuple = (3,1,4,1,5,9)

# new_tuple = list(pi_tuple)
# new_list = tuple(new_tuple)

# #can still use the same things


# # Dictionaries
# # UNique key for each value, cannot join dictionaries together

# super_villians = {'Fiddler' : "Issac Bowin",
#                     'add more' : "test"}

# print(super_villians["Fiddler"])
# # get a key super_villians.get("Key")
# # list of keys super_villians.keys()

# # conditionals

# age = 22

# if age > 16 :
#     print('You are old enough to drive')
# elif age >= 21 :
#     print('Old enough to drink')
# else :
#     print('Not old enough')

#     #and or not (logical operators) written as words not()

# # looping

# for x in range(0,10) :
#     print(x, ' ',end="")

# print("spacer")

# for y in grocery_list :
#     print(y)

# # for x in [2,4,6,8,10] :
# #     print(x)

# # while loops

# random_number = random.randrange(0,100)

# # while(random_number != 15) :
# #     print(random_number)
# #     random_number = random.randrange(0,100)

# # break is a keyword to break out of loop


# #functions

# def addNumber(fNum,lNum):
#     sumNum = fNum + lNum
#     return sumNum

# print(addNumber(5,6))

# # user input

# # print('what is your name')
# # name = sys.stdin.readline()

# long_strink = "This is a string that is quite long"

# print(long_strink[0:4])

# test_file = open("test.txt", "wb")

# print(test_file.mode)

# print(test_file.name)

# test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# test_file.close()

# test_file = open("test.txt", "r+")

# text_in_file = test_file.read()

# print(text_in_file)

# os.remove("test.txt")


# Objects and Classes

# __Name (private variables)

class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name) :
        self.__name = name

    def get_name() :
        return self.__name

    def set_height(self, height) :
        self.__height = height

    def get_height() :
        return self.__height

    def set_weight(self,weight):
        self.__weight = weight
    
    def get_weight():
        return self.__weight

    def set_name(self, sound) :
        self.__sound = sound

    def get_sound():
        return self.__sound

    def get_type():
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {}".format(self.__name,self.__height,self.__sound)

cat = Animal('Whiskers',33,10,'meow')

print(cat.toString())