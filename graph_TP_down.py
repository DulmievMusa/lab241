from mnk import *
from my_library import *
from math import pi, log
import matplotlib.pyplot as plt

beta = 40.7

h_es, T_es = get_all_columns_from_file("data_down.csv")
h_es = [133.3 * h for h in h_es]
T_es = [273+T for T in T_es]

plt.scatter(T_es, h_es)



k, b, dk, db = linear_regression(T_es, h_es)

#paint_line_function(k, b, T_es, y_es=h_es, color_number=8, size=4)



#plt.scatter(T_es, h_es)



set_end(y_label="$P, Па$", x_label="$T, К$")