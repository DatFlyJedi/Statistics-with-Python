from scipy.stats import norm


def proportion_z_test(sample_proportion, population_proportion, n):
    # Calculate standard error
    std_error = ((population_proportion * (1 - population_proportion)) / n) ** 0.5

    # Calculate z-score
    z_score = (sample_proportion - population_proportion) / std_error

    # Calculate p-value
    p_value = 2 * (1 - norm.cdf(abs(z_score)))  # Two-tailed test

    return z_score, p_value


# Given data
population_proportion = 0.05
sample_size = 395
sample_spam_count = 30
sample_proportion = sample_spam_count / sample_size

# Calculate z-score and p-value
z_score, p_value = proportion_z_test(sample_proportion, population_proportion, sample_size)

# Print results
print(f"Sample proportion: {sample_proportion}")
print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")

# Determine conclusion based on significance levels
alpha_1 = 0.1
alpha_2 = 0.05

if p_value < alpha_1:
    print(f"At {alpha_1} level of significance: Reject the null hypothesis.")
else:
    print(f"At {alpha_1} level of significance: Fail to reject the null hypothesis.")

if p_value < alpha_2:
    print(f"At {alpha_2} level of significance: Reject the null hypothesis.")
else:
    print(f"At {alpha_2} level of significance: Fail to reject the null hypothesis.")