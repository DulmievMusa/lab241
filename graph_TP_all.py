from mnk import *
from my_library import *
from math import pi, log
import matplotlib.pyplot as plt

beta = 40.7

h_es, T_es = get_all_columns_from_file("data_up.csv")
h_es = [133.3 * h for h in h_es]
T_es = [273+T for T in T_es]

plt.scatter(T_es, h_es, label="Нагревание")



h_es, T_es = get_all_columns_from_file("data_down.csv")
h_es = [133.3 * h for h in h_es]
T_es = [273+T for T in T_es]

plt.scatter(T_es, h_es, label="Охлаждение")



set_end(y_label="$P, Па$", x_label="$T, К$")