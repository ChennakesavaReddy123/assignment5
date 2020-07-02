# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 19:16:00 2020

@author: Chennakesava Reddy
"""

#3)write a  simple python program to read the contents of a file using statement
fh = open("sample_log.txt", "w") 
try: 
   fh.write("I love Python Programming!") 
finally: 
   fh.close()

with open("sample_log.txt", "w") as fh: 
   fh.write("I love Python even more!!")
