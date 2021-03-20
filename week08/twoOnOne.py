import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
# I prefer putting the abolute values into variables that are set at the top
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

plt.scatter(ages, salaries)
#plt.show() # if you do this the proram will halt here until the plot is closed

# add x squared
xpoints = np.array(range(1, 4))
ypoints = xpoints * xpoints  # multiply each entry by itself
hpoints = xpoints
gpoints = xpoints*xpoints*xpoints
plt.plot(xpoints, ypoints, hpoints, color= 'r')
plt.plot(xpoints, hpoints, color= 'g')
plt.plot(xpoints, gpoints, color= 'y')
plt.show() # see how the axis have changed