# ASSIGNMENT A06 - SEABORN FUNCTIONS

import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load dataset
df = sb.load_dataset('iris')

print("----- DATASET HEAD -----")
print(df.head())


# 1. HISTOGRAM
print("----- HISTOGRAM -----")
sb.histplot(df['petal_length'], kde=False)
plt.title("Histogram of Petal Length")
plt.show()


# 2. KDE (KERNEL DENSITY ESTIMATION)
print("----- KDE PLOT -----")
sb.kdeplot(df['petal_length'], fill=True)
plt.title("KDE Plot")
plt.show()


# 3. JOINT PLOT (SCATTER)
print("----- JOINT PLOT (SCATTER) -----")
sb.jointplot(x='petal_length', y='petal_width', data=df)
plt.show()


# 4. HEXBIN PLOT
print("----- HEXBIN PLOT -----")
sb.jointplot(x='petal_length', y='petal_width', data=df, kind='hex')
plt.show()


# 5. FACET GRID
print("----- FACET GRID -----")
tips = sb.load_dataset('tips')
g = sb.FacetGrid(tips, col="time")
g.map(sb.histplot, "total_bill")
plt.show()


# 6. PAIR GRID
print("----- PAIR GRID -----")
g = sb.PairGrid(df)
g.map(plt.scatter)
plt.show()


# 7. COLOR PALETTE
print("----- COLOR PALETTE -----")
palette = sb.color_palette("husl", 8)
sb.palplot(palette)
plt.show()


# 8. STYLE SETTINGS
print("----- STYLE SETTINGS -----")
sb.set_style("whitegrid")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Styled Plot using Seaborn")
plt.show()

print("----- PROGRAM COMPLETED -----")
