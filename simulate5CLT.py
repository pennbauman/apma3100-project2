# APMA 3100-006 S2020 Project 2
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian
#
# Part 5: Central Limit Theorem

from math import log, sqrt, pi
from rand18bit import rand18bit


### General variables (settings of simulation)
# Sample sizes
n = [10, 30, 50, 100, 150, 250, 500, 1000]

# NOTE: Need the 110 samples from part 4
M_n = []

# 2.1) Transform the given sample M_n into Z_n
a = 1/57
mean = 1/a * sqrt(pi/2) # Need to check
stdev = (4-pi)/(2a**2) # Need to check

def to_Z_n(n, m_n):
    return (m_n - mean)/(stdev/sqrt(n))

Z_n = []
## For each M_n
    # Call to_Z_n for size n
    # Save result in Z_n array


# 2.2) Estimate from the sample of Z_n the probabilities of seven events z

# Phi values for each event z_j (from table)
phi_z = {
  −1.4: 0.0808,
  −1.0: 0.1587,
  −0.5: 0.3085,
  0: 0.5,
  0.5: 0.6915,
  1.0: 0.8413,
  1.4: 0.9192
}

## For each Z_n
    # Iterate through z_j values in phi_z
        # Find P[Z_n <= z]
        # Find abs difference |F(z_j) - phi_z|
    # Get max abs diff (MAD) out of the 7

# 2.3) Evaluate the goodness-of-fit of the standard normal CDF 𝛷 to the
# empirical CDF 𝐹_𝑛 in terms of the maximum absolute difference MAD_n

# Done above in the for loop
