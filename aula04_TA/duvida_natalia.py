import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-20,21)
plt.subplot(2,2,1)
plt.plot(x,x)
plt.subplot(2,2,2)
plt.bar(x,x**2)
plt.subplot(2,2,4)
plt.scatter(x,x**3,linewidth = 3)
plt.show()
