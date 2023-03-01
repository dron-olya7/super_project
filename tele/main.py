import matplotlib
from IPython.display import display
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import os
import shutil
import posixpath

import wfdb

# Demo 1 - Read a WFDB record using the 'rdrecord' function into a wfdb.Record object.
# Plot the signals, and show the data.
#record = wfdb.rdrecord('sample-data/a103l')
#wfdb.plot_wfdb(record=record, title='Record a103l from PhysioNet Challenge 2015')
#display(record.__dict__)

# Can also read the same files hosted on PhysioNet https://physionet.org/content/challenge-2015/1.0.0
# in the /training/ database subdirectory.
record2 = wfdb.rdrecord('a103l', pn_dir='challenge-2015/training/', sampto=2000)
wfdb.plot_wfdb(record=record2, title='Record a103l from PhysioNet Challenge 2015')
#wfdb.plot_wfdb(record2)