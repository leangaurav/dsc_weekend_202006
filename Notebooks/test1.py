import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plot multiple graphs on same figure
data =  pd.Series([1,4,3,5,6,5,4,1,2,3,4]) ** 2
data2  = data/2

plt.figure(figsize=(16,3))

plt.subplot(1,2, 2)
plt.plot(data.index,data.values)

plt.subplot(1,2, 1)
plt.plot(data2.index,data2.values, 'g^')
plt.show()
