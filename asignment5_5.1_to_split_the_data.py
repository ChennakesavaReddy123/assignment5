# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 19:16:00 2020

@author: Administrator
"""



#1.write asimple rogram to split the data

def split_string(string): 

    list_string = string.split(' ') 

      

    return list_string 

  

def join_string(list_string): 


    string = '-'.join(list_string) 

      

    return string 

if __name__ == '__main__': 

    string = 'king of the king'

    list_string = split_string(string) 

    print(list_string) 

  

     

    new_string = join_string(list_string) 

    print(new_string)  