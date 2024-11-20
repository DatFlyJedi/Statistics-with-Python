import math
from scipy.stats import norm
from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 50

"p test is for two tailed test half the value for one tailed test"

def z_test(sample_mean, population_mean, std_dev, sample_size, alpha):
    # Convert all inputs to Decimals for high precision calculations
    sample_mean = Decimal(sample_mean)
    population_mean = Decimal(population_mean)
    std_dev = Decimal(std_dev)
    sample_size = Decimal(sample_size)
    alpha = Decimal(alpha)

    # Calculate the z-score
    z_score = (sample_mean - population_mean) / (std_dev / sample_size.sqrt())

    # Calculate the critical value from the z-distribution using float for compatibility
    critical_value = Decimal(norm.ppf(1 - float(alpha) / 2))

    # Calculate the p-value using float for compatibility
    p_value = Decimal(2) * (Decimal(1) - Decimal(norm.cdf(float(abs(z_score)))))

    # Determine whether to reject the null hypothesis
    if abs(z_score) > critical_value:
        conclusion = "Reject the null hypothesis."
    else:
        conclusion = "Fail to reject the null hypothesis."

    return z_score, critical_value, p_value, conclusion


# Example usage
sample_mean = 69.3  # Sample mean
population_mean = 69.4  # Population mean
std_dev = 2.11  # Population standard deviation
sample_size = 304  # Sample size
alpha = 0.05  # Significance level

z_score, critical_value, p_value, conclusion = z_test(sample_mean, population_mean, std_dev, sample_size, alpha)

print(f"Z-score: {z_score}")
print(f"Critical value: {critical_value}")
print(f"P-value: {p_value}")
print(f"Conclusion: {conclusion}")
