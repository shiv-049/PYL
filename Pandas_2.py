# ASSIGNMENT A02 - Pandas Functions

import pandas as pd
import numpy as np

print("----- SERIES CREATION -----")
# 1. Empty Series
s1 = pd.Series()
print("Empty Series:\n", s1)

# 2. Series from ndarray
data = np.array(['a', 'b', 'c', 'd'])
s2 = pd.Series(data)
print("Series from ndarray:\n", s2)

# 3. Series with custom index
s3 = pd.Series(data, index=[100, 101, 102, 103])
print("Series with custom index:\n", s3)


print("\n----- DATAFRAME CREATION -----")
# 4. Empty DataFrame
df1 = pd.DataFrame()
print("Empty DataFrame:\n", df1)

# 5. DataFrame from dictionary
d = {
    'Name': pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack','Lee','David','Gasper','Betina','Andres']),
    'Age': pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating': pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
df2 = pd.DataFrame(d)
print("DataFrame:\n", df2)


print("\n----- PANEL CREATION -----")
# 6. Panel (Note: Deprecated in new versions, but for exam purpose)
data_panel = np.random.rand(2,4,5)
try:
    p = pd.Panel(data_panel)
    print("Panel:\n", p)
except:
    print("Panel is deprecated in latest Pandas versions")


print("\n----- SERIES BASIC FUNCTIONS -----")
s = pd.Series(np.random.randn(4))
print("Series:\n", s)

print("Axes:", s.axes)
print("Dtype:", s.dtype)
print("Empty:", s.empty)
print("Dimensions:", s.ndim)
print("Size:", s.size)
print("Values:\n", s.values)
print("Head:\n", s.head())
print("Tail:\n", s.tail())


print("\n----- DESCRIPTIVE STATISTICS -----")
print("Count:\n", df2.count())
print("Sum:\n", df2.sum(numeric_only=True))
print("Mean:\n", df2.mean(numeric_only=True))
print("Median:\n", df2.median(numeric_only=True))
print("Mode:\n", df2.mode(numeric_only=True))
print("Standard Deviation:\n", df2.std(numeric_only=True))
print("Minimum:\n", df2.min(numeric_only=True))
print("Maximum:\n", df2.max(numeric_only=True))
print("Absolute:\n", df2.abs(numeric_only=True))
print("Product:\n", df2.prod(numeric_only=True))
print("Cumulative Sum:\n", df2.cumsum(numeric_only=True))
print("Cumulative Product:\n", df2.cumprod(numeric_only=True))

print("\n----- PROGRAM COMPLETED -----")
