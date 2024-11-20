import numpy as np
import scipy.stats as stats

# Scores before and after the class
scores_before = np.array([1351, 5.90, 4.14, 4.54, 5.29, 4.54])
scores_after = np.array([3.90, 5.49, 3.78, 4.12, 4.97, 3.95])

# Calculate the differences
differences = scores_after - scores_before

# Mean and standard deviation of differences
mean_diff = np.mean(differences)
std_diff = np.std(differences, ddof=1)

# Hypothesized difference
hypothesized_diff = 0

# Number of subjects
n = len(differences)

# Calculate the t-statistic
t_stat = (mean_diff - hypothesized_diff) / (std_diff / np.sqrt(n))

# Degrees of freedom
df = n - 1

# Calculate the p-value for a two-tailed test
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

# Print the results
print(f"Mean of differences: {mean_diff:.4f}")
print(f"Standard deviation of differences: {std_diff:.4f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"degrees of freedom: {df}")
print(f"p-value: {p_value:.4f}")

# Conclusion
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
