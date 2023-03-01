import matplotlib
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import posixpath

import wfdb

a = input("Enter the name of file, for example 100:\n")
print("You chose file: ",a)

b = input("Enter the name of the Physionet database directory from which to find the required record files for example: mitdb/1.0.0:\n")
print("You chose Physionet directory: ",b)
#record2 = wfdb.rdrecord('100', pn_dir='mitdb/1.0.0', sampto=1000)

record2 = wfdb.rdrecord(a, pn_dir=b, sampto=1000)
wfdb.plot_wfdb(record=record2, title=f'Record {a} from PhysioNet mitdb')

