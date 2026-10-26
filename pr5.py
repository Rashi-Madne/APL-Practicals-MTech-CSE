import pandas as pd
import numpy as np

# TASK 1: Load dataset and display basic information
iris = pd.read_csv("Iris.csv")

print("\n--- TASK 1: LOAD DATASET ---")
print("Shape:", iris.shape)
print("Type:", type(iris))
print("\nFirst 4 rows:\n", iris.head(4))
print("\nLast 4 rows:\n", iris.tail(4))

# TASK 2: Replace abnormal symbols with NaN
print("\n--- TASK 2: REPLACE ABNORMAL SYMBOLS ---")
iris = iris.replace(["??", "##"], np.nan)

# Convert measurement columns to numeric values
numeric_columns = [
    "SepalLengthCm", "SepalWidthCm",
    "PetalLengthCm", "PetalWidthCm"
]

for col in numeric_columns:
    iris[col] = pd.to_numeric(iris[col], errors="coerce")

print("Abnormal symbols replaced with NaN.")
print(iris.head(4))

# TASK 3: Describe dataset and count observations and missing values
print("\n--- TASK 3: DATASET DESCRIPTION ---")
print(iris.describe(include="all"))
print("Number of observations:", iris.shape[0])
print("\nMissing values in each column:\n", iris.isnull().sum())
print("Total missing values:", iris.isnull().sum().sum())
print("\nNaN values in each column:\n", iris.isna().sum())

# TASK 4: Statistical details of the complete dataset
print("\n--- TASK 4: STATISTICS OF COMPLETE DATASET ---")
print("\nPercentiles:\n", iris[numeric_columns].quantile([0.25, 0.50, 0.75]))
print("\nMean:\n", iris[numeric_columns].mean())
print("\nStandard deviation:\n", iris[numeric_columns].std())
print("\nMode:\n", iris[numeric_columns].mode())
print("\nVariance:\n", iris[numeric_columns].var())
print("\nSkewness:\n", iris[numeric_columns].skew())
print("\nKurtosis:\n", iris[numeric_columns].kurt())

# TASK 5: Statistics of each species
print("\n--- TASK 5: SPECIES-WISE STATISTICS ---")
for species in ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]:
    data = iris.loc[iris["Species"] == species, numeric_columns]
    print("\nSpecies:", species)
    print("Percentiles:\n", data.quantile([0.25, 0.50, 0.75]))
    print("Mean:\n", data.mean())
    print("Standard deviation:\n", data.std())
    print("Mode:\n", data.mode())
    print("Variance:\n", data.var())
    print("Skewness:\n", data.skew())
    print("Kurtosis:\n", data.kurt())

# TASK 6: Drop Id column
print("\n--- TASK 6: DROP ID COLUMN ---")
iris_no_id = iris.drop(columns=["Id"], errors="ignore")
print(iris_no_id.head())

# TASK 7: Species and row number with maximum Sepal Length
print("\n--- TASK 7: MAXIMUM SEPAL LENGTH ---")
max_index = iris["SepalLengthCm"].idxmax()
print("Species:", iris.loc[max_index, "Species"])
print("DataFrame row index:", max_index)
print("Row number (starting from 1):", max_index + 1)
print("Maximum Sepal Length:", iris.loc[max_index, "SepalLengthCm"])

# TASK 8: Species and row number with minimum Petal Width
print("\n--- TASK 8: MINIMUM PETAL WIDTH ---")
min_index = iris["PetalWidthCm"].idxmin()
print("Species:", iris.loc[min_index, "Species"])
print("DataFrame row index:", min_index)
print("Row number (starting from 1):", min_index + 1)
print("Minimum Petal Width:", iris.loc[min_index, "PetalWidthCm"])

# TASK 9: Sort rows by Sepal Length
print("\n--- TASK 9: SORT BY SEPAL LENGTH ---")
sorted_iris = iris.sort_values(by="SepalLengthCm")
print(sorted_iris)

# TASK 10: Replace missing values
print("\n--- TASK 10: FILL MISSING VALUES ---")
petal_mean = iris["PetalWidthCm"].mean()
sepal_mode = iris["SepalLengthCm"].mode()[0]

iris["PetalWidthCm"] = iris["PetalWidthCm"].fillna(petal_mean)
iris["SepalLengthCm"] = iris["SepalLengthCm"].fillna(sepal_mode)

print("Petal Width missing values filled with mean:", petal_mean)
print("Sepal Length missing values filled with mode:", sepal_mode)
print("\nMissing values after filling:\n", iris.isnull().sum())

# TASK 11: Pearson correlation without using a correlation library
print("\n--- TASK 11: PEARSON CORRELATION ---")
data = iris[["PetalWidthCm", "PetalLengthCm"]].dropna()

x = data["PetalWidthCm"]
y = data["PetalLengthCm"]

n = len(data)
sum_x = x.sum()
sum_y = y.sum()
sum_xy = (x * y).sum()
sum_x2 = (x ** 2).sum()
sum_y2 = (y ** 2).sum()

numerator = n * sum_xy - sum_x * sum_y

denominator = np.sqrt(
    (n * sum_x2 - sum_x ** 2) *
    (n * sum_y2 - sum_y ** 2)
)

if denominator != 0:
    r = numerator / denominator
    print("Pearson Correlation Coefficient:", r)
else:
    print("Correlation cannot be calculated.")


