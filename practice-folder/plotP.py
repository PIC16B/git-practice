from matplotlib import pyplot as plt
import numpy as np
<<<<<<< HEAD

#wrap plot script in function
def plot():
    x = np.linspace(0, 2*np.pi, 1001)
    y = np.sin(x)
    m = np.linspace(0, 2*np.pi, 1001)
    n = np.sin(m)
    f = plt.plot(m,n)
plot()
