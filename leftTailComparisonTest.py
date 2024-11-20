import scipy.stats as stats

# Given data
n1 = 82
mean1 = 3.2
std1 = 7.24

n2 = 84
mean2 = 5.0
std2 = 7.62

# Calculate the t-statistic
t_stat = (mean1 - mean2) / ((std1**2 / n1 + std2**2 / n2)**0.5)

# Degrees of freedom
df_num = (std1**2 / n1 + std2**2 / n2)**2
df_den = ((std1**2 / n1)**2 / (n1 - 1)) + ((std2**2 / n2)**2 / (n2 - 1))
df = df_num / df_den

# Calculate the p-value for a left-tailed test
p_value = stats.t.cdf(t_stat, df)

# Print the results
print(f"t-statistic: {t_stat:.4f}")
print(f"degrees of freedom: {df:.4f}")
print(f"p-value: {p_value:.4f}")

# Conclusion
alpha = 0.1
if p_value < alpha:
    print("Reject the null hypothesis: The mean weight loss on the low-carb diet is significantly less than the mean weight loss on the low-fat diet.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in mean weight loss between the low-carb and low-fat diets.")
