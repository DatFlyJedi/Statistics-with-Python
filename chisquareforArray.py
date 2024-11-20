import numpy as np

# Observed frequency table
observed = np.array([
    [11, 11, 22],  # Influenza
    [8, 24, 14],   # Headache
    [69, 138, 213],   # Weakness
  # [,,]    # Shortness of Breath
])

# Step 2: Calculate row totals, column totals, and grand total
row_totals = observed.sum(axis=1)
column_totals = observed.sum(axis=0)
grand_total = observed.sum()

# Step 3: Calculate the expected frequency table
expected = np.outer(row_totals, column_totals) / grand_total

# Step 4: Calculate the chi-squared statistic
chi_squared_statistic = ((observed - expected) ** 2 / expected).sum()

chi_squared_statistic
print("Chi squared statistic=", {chi_squared_statistic})
print(expected)
"degree of freedom for this is one minus colum times one minus row"