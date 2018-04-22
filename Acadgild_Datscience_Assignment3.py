# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 01:28:29 2018

@author: ALOK
"""
# This python code converts lowercase to uppercase and uppercase to lowercase

#Sample input
myinput = "AltERNating"

#Function that converts lowercase to uppercase and uppercase to lowercase
def switch_lowerupper(string):
    output = ''
#iterated through each work in the string
    for word in string:

#Checks if work is upper, if true converts to lower by parsing
        if word.isupper():
            output += word.lower()
        else:
            output += word.upper()
    return output

print switch_lowerupper(myinput)
