from mnk import *
from my_library import *
from math import pi, log

beta = 40.7

h_es, T_es = get_all_columns_from_file("data_down.csv")
T_es = [1000/(T + 273) for T in T_es]
h_es = [log(h * 133.3) for h in h_es]

k, b, dk, db = linear_regression(T_es, h_es)



print("k", k)
print("dk", dk)
print("L", (k * 8.31)/1000)
paint_line_function(k, b, T_es, y_es=h_es, color_number=8, size=4)
#plt.scatter(T_es, h_es)



set_end(y_label="$\ln (P)$", x_label="$1/T, 10^{-3}  К^{-1}$")