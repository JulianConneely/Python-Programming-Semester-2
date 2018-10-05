# Julian Conneely 05/10/18
# Histograms

import matplotlib.pyplot as plt
import numpy as np

x = np.ormal(0.0, 1.0, 1000)

plt.hist(x, bins=20) # increase the no of bins or widens the histogram, (more intervals on tyhe x axis)

plt.show()
