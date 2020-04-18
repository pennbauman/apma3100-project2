# APMA 3100-006 S2020 Project 2
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian

from math import log, sqrt
from rand18bit import rand18bit


### General variables (settings of simulation)
## Number of simulations
n_options = [10, 30, 50, 100, 150, 250, 500, 1000]
# n_options = [10, 30]
n_experiments = 110
## Output settings
prints = 1
    # 0 none
    # 1 expectations
    # 2 results



## Distance from target value
##   x(F) = sqrt((-2*ln(1 - F))/a^2)
def distance(F):
    a = 1/57
    return sqrt((-2*log(1 - F))/a**2)



### Generate table of random values
rands = rand18bit()

# print(rands.getU(51))
# print(rands.getU(52))
# print(rands.getU(53))

results = open("results.csv", "w")
for n in n_options:
    line = str(n) + ", "
    for e in range(n_experiments):
        count = 0
        for i in range(n):
            count += distance(rands.nextU())
        line += str(count/n) + ", "
    results.write(line + "\n")

# rands.print()
