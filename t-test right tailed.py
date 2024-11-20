from scipy.stats import t
from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 50

"subtract from 1 for left tailed test"

def t_test(sample_mean, population_mean, std_dev, sample_size, alpha):
    # Convert all inputs to Decimals for high precision calculations
    sample_mean = Decimal(sample_mean)
    population_mean = Decimal(population_mean)
    std_dev = Decimal(std_dev)
    sample_size = Decimal(sample_size)
    alpha = Decimal(alpha)

    # Calculate the t-score
    t_score = (sample_mean - population_mean) / (std_dev / sample_size.sqrt())

    # Calculate the degrees of freedom
    degrees_of_freedom = sample_size - 1

    # Calculate the p-value for a one-tailed test
    p_value = 1 - Decimal(t.cdf(float(t_score), int(degrees_of_freedom)))

    # Determine whether to reject the null hypothesis
    if p_value < alpha:
        conclusion = "Reject the null hypothesis."
    else:
        conclusion = "Fail to reject the null hypothesis."

    return t_score, p_value, conclusion


# Provided values
population_mean = 25  # Population mean
sample_mean = 24.4  # Sample mean
std_dev = 5.3  # Sample standard deviation
sample_size = 310  # Sample size
alpha = 0.1  # Significance level

t_score, p_value, conclusion = t_test(sample_mean, population_mean, std_dev, sample_size, alpha)

print(f"T-score: {t_score}")
print(f"P-value: {p_value}")
print(f"Conclusion: {conclusion}")