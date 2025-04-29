import numpy as np
from scipy import stats



data = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
data = list(map(int, data.split(" ")))
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)[0]
std = np.std(data)
z = 1.96

std_error = (std/np.sqrt(len(data)))
lower_bound = mean-z*std_error
upper_bound = mean+z*std_error


print("{:.1f}".format(mean))
print("{:.1f}".format(median))
print(mode)
print("{:.1f}".format(std))

print(f"{"{:.1f}".format(lower_bound)} {"{:.1f}".format(upper_bound)}")