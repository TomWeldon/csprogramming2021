import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100
#np.random.seed(1)
salaries = np.random.randint( minSalary, maxSalary, numberOfEntries)
'''
salariesPlus = salaries + 5000
salariesMult = salaries * 1.05
newSalaries = salariesMult.astype(int)

print(salaries)
print(salariesPlus)
print(newSalaries)
'''
plt.hist(salaries, color = 'g')

plt.show()
