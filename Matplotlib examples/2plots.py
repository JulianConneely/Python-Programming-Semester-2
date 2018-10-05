# Julian Conneely 05/10/18
# Two plots on one set of axes

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.') # calls plot function once. r. uses a red dot instead of the default line in the plot
plt.plot(x, y, 'b-') # calls plot function second time. b- indicates a blue line

plt.show() # calls the show function obviously