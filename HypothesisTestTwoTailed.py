import numpy as np
import scipy.stats as stats

# Given data
n1 = 6663  # number of boys
x1 = 651   # number of overweight boys
n2 = 6725  # number of girls
x2 = 577   # number of overweight girls

# Calculate the sample proportions
p1_hat = x1 / n1
p2_hat = x2 / n2

# Calculate the pooled proportion
p_hat = (x1 + x2) / (n1 + n2)

# Calculate the standard error
SE = np.sqrt(p_hat * (1 - p_hat) * (1/n1 + 1/n2))

# Calculate the z-statistic
z = (p1_hat - p2_hat) / SE

# Calculate the p-value for a right-tailed test
p_value = 2 * (1 - stats.norm.cdf(z))

# Print the results
print(f"Proportion of overweight boys: {p1_hat:.4f}")
print(f"Proportion of overweight girls: {p2_hat:.4f}")
print(f"z-statistic: {z:.4f}")
print(f"p-value: {p_value:.4f}")

# Conclusion
alpha = 0.1
if p_value < alpha:
    print("Reject the null hypothesis: The proportion of overweight boys is greater than the proportion of overweight girls.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in the proportion of overweight boys and girls.")
