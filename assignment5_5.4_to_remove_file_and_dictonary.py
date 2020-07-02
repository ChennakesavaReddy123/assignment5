# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 19:16:00 2020

@author: Chennakesava Reddy
"""

#python prograam to remove file and dictonary


import os
myfile="/tmp/foo.txt"


if os.path.isfile(myfile):
    os.remove(myfile)
else:    
    print("Error: %s file not found" % myfile)