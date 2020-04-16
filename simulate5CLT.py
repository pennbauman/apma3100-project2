# APMA 3100-006 S2020 Project 2
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian
#
# Part 5: Central Limit Theorem

from math import log, sqrt, pi
from rand18bit import rand18bit
import csv


### General variables (settings of simulation)
# Sample sizes
sample_size = [10, 30, 50, 100, 150, 250, 500, 1000]
TOTAL_SAMPLES = 110

# NOTE: Need the 110 samples from part 4
M_n = {} # sample_size: [110 sample means]
with open('sample_means.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for i, row in enumerate(csv_reader):
        values = []
        for item in row:
            values.append(float(item))
        M_n[values[0]] = values[1:]
# print(M_n)

##### 2.1) Transform the given sample M_n into Z_n
a = 1/57
mean = (1/a) * sqrt(pi/2) # Need to check
stdev = sqrt((4-pi)/(2 * (a**2))) # Need to check

def to_Z_n(n, m_n):
    return (m_n - mean)/(stdev/sqrt(n))

## For each M_n
    # Call to_Z_n for size n
    # Save result in Z_n array
Z_n = {}
for n, samples in M_n.items():
    z_values = []
    for m in samples:
        z_values.append(to_Z_n(n, m))
    Z_n[n] = z_values
# print(Z_n)

##### 2.2) Estimate from the sample of Z_n the probabilities of seven events z

# Phi values for each event z_j (from table)
phi_values = {
  -1.4: 0.0808,
  -1.0: 0.1587,
  -0.5: 0.3085,
  0: 0.5,
  0.5: 0.6915,
  1.0: 0.8413,
  1.4: 0.9192
}

F_n = {}
for n, z_values in Z_n.items():
    probs = {}
    # Iterate through z_j values in phi_z
    for z_j in phi_values:
        amount_lower = 0
        # Find P[Z_n <= z]
        for z in z_values:
            if z < z_j:
                amount_lower += 1
        probs[z_j] = amount_lower/TOTAL_SAMPLES
    F_n[n] = probs
# print(F_n)


##### 2.3) Evaluate the goodness-of-fit of the standard normal CDF 𝛷 to the
# empirical CDF 𝐹_𝑛 in terms of the maximum absolute difference MAD_n

AD_n = {}
MAD_n = {}

for n, f_values in F_n.items():
    ad_values = {}
    mad_value = 0
    # Iterate through probabilities for each z_j and compare to phi values
    for z_j, f_z in f_values.items():
        # Find abs difference |F(z_j) - phi_z|
        absolute_difference = abs(f_z - phi_values[z_j])
        ad_values[z_j] = absolute_difference
        mad_value = max(mad_value, absolute_difference)
    # Get max abs diff (MAD) out of the 7
    AD_n[n] = ad_values
    MAD_n[n] = mad_value
# print(AD_n)
# print(MAD_n)

##### Output values to CSV format
with open('ad_data.csv', 'w') as outfile:
    outfile.write('n,-1.4,-1.0,-0.5,0,0.5,1.0,1.4,MAD\n')
    for n, ad_values in AD_n.items():
        outfile.write(str(n) + ',')
        for z_j, ad in ad_values.items():
            outfile.write(str(ad) + ',')
        outfile.write(str(MAD_n[n]) + ',')
        outfile.write('\n')
