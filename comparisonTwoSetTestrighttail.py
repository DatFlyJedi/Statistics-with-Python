import numpy as np
import scipy.stats as stats

# Pain ratings for each subject
drug_a = np.array([1351, 1355, 1301, 1330, 1327])
drug_b = np.array([1343, 1377, 1367, 1350, 1389])

# Calculate the differences
differences = drug_a - drug_b

# Mean and standard deviation of differences
mean_diff = np.mean(differences)
std_diff = np.std(differences, ddof=1)

# Number of subjects
n = len(differences)

# Calculate the t-statistic
t_stat = mean_diff / (std_diff / np.sqrt(n))

# Degrees of freedom
df = n - 1

# Calculate the p-value for a right-tailed test
p_value = 1 - stats.t.cdf(t_stat, df)

# Print the results
print(f"Mean of differences: {mean_diff:.4f}")
print(f"Standard deviation of differences: {std_diff:.4f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"degrees of freedom: {df}")
print(f"p-value: {p_value:.4f}")

# Conclusion
alpha = 0.1
if p_value < alpha:
    print("Reject the null hypothesis: The mean pain level with drug A is greater than with drug B.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in mean pain levels between drug A and drug B.")