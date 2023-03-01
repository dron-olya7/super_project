import matplotlib
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import posixpath
import sys

import wfdb

namefile = ""
directory = ""
sempling = 1000

if(len(sys.argv) <= 2):
    #новый коммент
    #пользователь вводит название файла
    namefile = input("Enter the name of file, for example 100:\n")
    print("You chose file: ",a)

    #пользователь вводит директорию 
    directory = input("Enter the name of the Physionet database directory from which to find the required record files for example: mitdb/1.0.0:\n")
    print("You chose Physionet directory: ",b)  
    

if(len(sys.argv) >= 3):

    i = 1
    while i < len(sys.argv):
    
        if(sys.argv[i] == "-s"):
            sempling = int(sys.argv[i + 1])
            i += 2     
        if(sys.argv[i] == "-i"):
            namefile = sys.argv[i + 1]
            i += 2
            
        if(sys.argv[i] == "-d"):
            directory = sys.argv[i + 1]
            i += 2 
          

record2 = wfdb.rdrecord(namefile, pn_dir=directory, sampto=sempling)
wfdb.plot_wfdb(record=record2, title=f'Record {namefile} from PhysioNet mitdb')

