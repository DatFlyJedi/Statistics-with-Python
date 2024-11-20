import scipy.stats as stats

# Given data
n1 = 1010
mean1 = 10.45
std1 = 14.99

n2 = 1079
mean2 = 9.63
std2 = 13.34

# Calculate the t-statistic
t_stat = (mean1 - mean2) / ((std1**2 / n1 + std2**2 / n2)**0.5)

# Degrees of freedom
df_num = (std1**2 / n1 + std2**2 / n2)**2
df_den = ((std1**2 / n1)**2 / (n1 - 1)) + ((std2**2 / n2)**2 / (n2 - 1))
df = df_num / df_den

# Calculate the p-value
p_value = (1 - stats.t.cdf(abs(t_stat), df))

# Print the results
print(f"t-statistic: {t_stat:.4f}")
print(f"degrees of freedom: {df:.4f}")
print(f"p-value: {p_value:.4f}")

# Conclusion
alpha = 0.1
if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")