from my_library import *
from mnk import *
from math import log as ln

h_es, T_es = get_all_columns_from_file("data_down.csv")

print("| t | T | delta_h | P | 1/T | ln(P) |")
for i in range(len(h_es)):
    print(f"| {T_es[i]} | {my_round(T_es[i] + 273.15, 1)} | {h_es[i]} | {my_round(h_es[i] * 133.3, 1)} | {my_round(1/(T_es[i]+273.15) * 1000, 3)} | {my_round(ln(h_es[i] * 133.3), 2)} |")