# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 1
# Date: 5/10/2026
# Description: Collect flu case counts for 7 days, compute total, average, min, max, and rolling mean.

# 1
print("\n1: Use pandas to convert the list into a Series and call .describe() to get a statistical summary.")
import pandas as pd

counts = [19, 22, 25, 18, 20, 24, 21]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

total = sum(counts)
avg = sum(counts) / len(counts)
print('Total:', total, 'Avg:', round(avg, 2), 'Min:', min(counts), 'Max:', max(counts))

series_counts = pd.Series(counts)
print(series_counts.describe())

# 2
print("\n2: Plot the 3-day rolling mean of the counts with matplotlib. ")
import matplotlib.pyplot as plt

rolling = []
for i in range(2, len(counts)):
    rolling.append(round((counts[i-2] + counts[i-1] + counts[i]) / 3, 2))
print("3-day rolling mean:", rolling)

plt.plot(days[2:], rolling, marker='o', linestyle='-', color='red')
plt.title('3-Day Rolling Mean of Flu Cases')
plt.xlabel('Day')
plt.ylabel('Average Cases')
plt.grid(True)
plt.show() 

# 3
print("\n3: Detect anomalies where cases differ from the mean by more than 2 × standard deviation.")
mean_val = series_counts.mean()
std_dev = series_counts.std()

print(f"Mean: {mean_val:.2f}, Std Dev: {std_dev:.2f}")
print("Anomalies (> 2 std dev from mean):")

anomaly_found = False
for day, count in zip(days, counts):
    if abs(count - mean_val) > 2 * std_dev:
        print(f"{day}: {count} cases")
        anomaly_found = True

if not anomaly_found:
    print("No anomalies detected this week.")

# 4
print("\n4: Compare current week's data with the previous week's data.")
prev_counts = [15, 18, 20, 19, 17, 22, 18] # Assumed previous week data

print(f"{'Day':<5}{'Prev':>6}{'Curr':>6}{'% Change':>12}")
print("-" * 30)
for d, p, c in zip(days, prev_counts, counts):
    pct_change = ((c - p) / p) * 100
    print(f"{d:<5}{p:>6}{c:>6}{pct_change:>11.2f}%")

# 5
print("\n5: Save the data to a CSV file named 'flu_counts.csv'.")
import csv

filename = "flu_counts.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Cases"]) 
    for day, count in zip(days, counts):
        writer.writerow([day, count])

print(f"Successfully saved data to {filename}")