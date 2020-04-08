# APMA 3100-006 S2020 Project 2
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian

from math import log, sqrt
from rand16bit import rand16bit


### General variables (settings of simulation)
## Number of simulations
n_options = [10, 30, 50, 100, 150, 250, 500, 1000]
# n_options = [10, 30]
## Output settings
prints = 0
    # 0 none
    # 1 results



## Distance from target value
##   x(F) = sqrt((-2*ln(1 - F))/a^2)
def distance(F):
    a = 1/57
    return sqrt((-2*log(1 - F))/a**2)



### Generate table of random values
rands = rand16bit()

# print(rands.getU(51))
# print(rands.getU(52))
# print(rands.getU(53))

for n in n_options:
    results = open("results_n{:04d}.csv".format(n), "w")
    results.write("trial, distance\n")
    print("Number: " + str(n))
    ## Iterate over number options
    # count = 0
    for i in range(n):
        ## Initialize trial
        x = distance(rands.nextU())
        results.write(str(i) + ", " + str(x) + "\n")
        if (prints == 1):
            print("x(" + str(i) + "): " + str(x))
        # count += x

    if (prints == 1):
        print("E[X] = " + str(count/n))
        print()

