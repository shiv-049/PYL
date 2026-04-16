# ASSIGNMENT A03 - Matplotlib Functions

import matplotlib.pyplot as plt
import numpy as np

print("----- BASIC LINE PLOT -----")
# 1. Simple line from (0,0) to (6,250)
x1 = np.array([0, 6])
y1 = np.array([0, 250])
plt.plot(x1, y1)
plt.title("Simple Line Plot")
plt.show()


print("----- PLOT USING X AND Y -----")
# 2. Plot using x and y values
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)
plt.plot(x, y)
plt.title("Line using sin function")
plt.show()


print("----- PLOT WITH MARKERS ONLY -----")
# 3. Only markers
x2 = np.array([1, 8])
y2 = np.array([3, 10])
plt.plot(x2, y2, 'o')
plt.title("Markers Only")
plt.show()


print("----- MULTIPLE POINTS -----")
# 4. Multiple points
x3 = np.array([1, 2, 6, 8])
y3 = np.array([3, 8, 1, 10])
plt.plot(x3, y3)
plt.title("Multiple Points")
plt.show()


print("----- DEFAULT X VALUES -----")
# 5. Without x values
y4 = np.array([3, 8, 1, 10, 5, 7])
plt.plot(y4)
plt.title("Default X values")
plt.show()


print("----- LABELS AND TITLE -----")
# 6. Labels and Title
x5 = np.array([80, 85, 90, 95, 100])
y5 = np.array([240, 250, 260, 270, 280])
plt.plot(x5, y5)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Data")
plt.show()


print("----- GRID -----")
# 7. Grid
plt.plot(x5, y5)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Grid Example")
plt.grid()
plt.show()


print("----- HISTOGRAM -----")
# 8. Histogram
data = np.random.normal(170, 10, 250)
plt.hist(data)
plt.title("Height Distribution")
plt.show()


print("----- PIE CHART -----")
# 9. Pie chart
y6 = np.array([35, 25, 25, 15])
plt.pie(y6)
plt.title("Pie Chart Example")
plt.show()


print("----- PROGRAM COMPLETED -----")
