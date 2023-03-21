from matplotlib import pyplot as plt
import numpy as np
#the next script creates a plot
x = np.linspace(0, 2*np.pi, 1001)
y = np.sin(x)
m = np.linspace(0, 2*np.pi, 1001)
n = np.sin(m)
f = plt.plot(m,n)
