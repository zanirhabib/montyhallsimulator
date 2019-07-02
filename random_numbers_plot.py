import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import random

numlist = []
num = []
percentages = []
numlist.append(random.randint(1,10))
for b in range(1,1000,1):
    numlist.append(random.randint(1,10))

for a in range(1,11,1):
    num.append(a)
    percentages.append(numlist.count(a))




plt.bar(num,percentages)
plt.show()