
#-*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import re
    
def lucky(sequence):
    #Break the sequence by '12347890', to stay only 5s and 6s
    lucky_series = re.split(r'[12347890]', str(sequence))

    #now we need to delete '' and single 5,6s digits
    #We use set() bacause its an unordered collection with no duplicate elements
    lucky_series = [i for i in lucky_series if len(set(i)) != 1 and len(set(i)) != 0]
    
    #Last step is find max lenght combintaion in sequence
    if len(lucky_series) == 0:
        print(0)
    else:
        print("lucky series is ", max(lucky_series, key=len))
lucky(1231235656561235555555555556)
                                                                     
                                                                     

