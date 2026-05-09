import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data_up.csv", sep=',')

T = 1/(data['T']+273)
h = data['h']

plt.scatter(T, np.log(h))

plt.show()