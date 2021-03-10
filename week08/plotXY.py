import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'red', label = 'x-squared')
plt.xlabel('xpoints')
plt.ylabel('ypoints')
plt.title('X-Y Plot', color ='b')
plt.legend()
plt.show()

