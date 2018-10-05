# Julian Conneely 05/10/18
# adding Title, Labels and Legend

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.', label="Actual") # added label
plt.plot(x, y, 'b-', label="Model") # added label

plt.title("Super Simple Plot") # title, labels and legend
plt.xlabel("weight")
plt.ylabel("height")
plt.legend()

plt.show() 