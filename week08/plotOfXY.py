import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array(range(1, 4))

#ypoints = xpoints * xpoints  # multiply each entry by itself
fpoints = xpoints
gpoints = xpoints * xpoints
hpoints = xpoints*xpoints*xpoints

plt.plot(xpoints, hpoints, color= 'g',label='Test')
plt.legend()
plt.plot(xpoints, gpoints, color= 'y', label= 'Test2')
plt.legend()
plt.plot(xpoints, fpoints, color= 'b')

plt.show()