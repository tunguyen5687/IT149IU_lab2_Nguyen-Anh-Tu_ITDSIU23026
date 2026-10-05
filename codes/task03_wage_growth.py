# Student Name: Nguyễn Anh Tú
# Student ID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 3
# Date: 5/10/2026
# Description: Simulate yearly wage increase with a compound growth formula and format tabular output.

# 1
o = float(input("Enter starting wage: "))
p = float(input("Enter annual growth rate: "))
years = int(input("Enter number of years: "))

print(f"{'Year':<6}{'Wage ($/hr)':>12}")
print("-" * 18)
for n in range(1, years + 1):
    w = o * (1 + p) ** n
    print(f"{n:<6}{w:>12.2f}")

# 2
o, p = 10.0, 0.03
prev_w = o  # Keep track of previous year's wage

print(f"{'Year':<6}{'Wage ($/hr)':>12}{'Increase':>12}")
print("-" * 30)
for n in range(1, 11):
    w = o * (1 + p) ** n
    increase = w - prev_w
    print(f"{n:<6}{w:>12.2f}{increase:>12.2f}")
    prev_w = w  # Update for next iteration

# 3
import matplotlib.pyplot as plt

o, p = 10.0, 0.03
years_list = list(range(1, 11))
wages = []

for n in years_list:
    wages.append(o * (1 + p) ** n)

plt.figure(figsize=(6, 4))
plt.plot(years_list, wages, marker='o', color='blue')
plt.title('Wage Growth Over 10 Years (3% Raise)')
plt.xlabel('Year')
plt.ylabel('Wage ($/hr)')
plt.grid(True)
plt.show()

# 4
rates = [0.02, 0.05, 0.08]
o = 10.0

plt.figure(figsize=(8, 5))
for rate in rates:
    wages_at_rate = [o * (1 + rate) ** n for n in years_list]
    plt.plot(years_list, wages_at_rate, marker='s', label=f'{rate*100}% Raise')

plt.title('Wage Growth Comparison')
plt.xlabel('Year')
plt.ylabel('Wage ($/hr)')
plt.legend()
plt.grid(True)
plt.show()

# 5
o = 10.0
p = 0.03
inflation_rate = 0.02
real_growth_rate = p - inflation_rate

print(f"{'Year':<6}{'Nominal':>12}{'Real Wage':>12}")
print("-" * 30)
for n in range(1, 11):
    nominal_w = o * (1 + p) ** n
    real_w = o * (1 + real_growth_rate) ** n
    print(f"{n:<6}{nominal_w:>12.2f}{real_w:>12.2f}")