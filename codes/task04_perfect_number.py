# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 4
# Date: 5/10/2026
# Description: Check whether a number is a perfect number using divisor summation optimized up to square root of n.

#  Ask the user to input a number and test it
def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    return s == n

for n in [6, 28, 12]:
    print(n, is_perfect(n))
    
user_n = int(input("Enter a number to check: "))
print(f"Is {user_n} perfect? {is_perfect(user_n)}")

# List all perfect numbers between 1 and 10000.
# Count how many perfect numbers exist in a given range.
perfect_nums = []
for num in range(1, 10001):
    if is_perfect(num):
        perfect_nums.append(num)

print(f"Perfect numbers between 1 and 10000: {perfect_nums}")
print(f"Total count: {len(perfect_nums)}")

# Add an iteration counter to display how many divisors were checked.
def is_perfect_counted(n: int):
    if n < 2:
        return False, 0
    s = 1
    i = 2
    iterations = 0
    while i * i <= n:
        iterations += 1  
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    return s == n, iterations

test_val = 28
is_perf, iters = is_perfect_counted(test_val)
print(f"Number: {test_val} | Is Perfect: {is_perf} | Divisors checked (iterations): {iters}")

# Plot the distribution of perfect numbers
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.plot(range(1, len(perfect_nums) + 1), perfect_nums, marker='o', color='blue', linestyle='-')
plt.title("Distribution of Perfect Numbers (up to 10000)")
plt.xlabel("Index of Perfect Number (1st, 2nd, 3rd...)")
plt.ylabel("Value of Perfect Number")
plt.grid(True)
plt.show()