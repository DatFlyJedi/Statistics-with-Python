import math

# Given data
x = 434  # number of successes
n = 1033  # sample size
p0 = 0.46  # hypothesized population proportion

# Calculate the sample proportion
p_hat = x / n

# Calculate the z-test statistic
z_statistic = (p_hat - p0) / math.sqrt((p0 * (1 - p0)) / n)
p_hat, z_statistic

print("p-hat", p_hat)
print("z-test statistic", z_statistic)