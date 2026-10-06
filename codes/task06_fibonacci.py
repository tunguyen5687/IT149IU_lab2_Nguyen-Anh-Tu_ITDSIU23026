# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 6
# Date: 5/10/2026
# Description: Generate the Fibonacci sequence iteratively and find the nth term using tuple assignment.

# 1
print("\n 1")
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
user_n = int(input("Enter n to find the nth Fibonacci number: "))
print(f"F({user_n}) = {fib(user_n)}")

# 2
print("\n 2")
for i in range(2, 16):
    ratio = fib(i) / fib(i-1)
    print(f"F({i})/F({i-1}) = {ratio:.6f}")

# 3
print("\n 3")
import matplotlib.pyplot as plt

n_vals = list(range(20))
fib_vals = [fib(i) for i in n_vals]

plt.figure(figsize=(7, 4))
plt.plot(n_vals, fib_vals, marker='o', color='green')
plt.title("Fibonacci Sequence Exponential Growth")
plt.xlabel("n (Index)")
plt.ylabel("F(n) Value")
plt.grid(True)
plt.show()

# 4
print("\n 4")
import time

def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

test_n = 35 # Use a sufficiently large number to see the delay

# Test Iterative (Teacher's method)
start_time = time.time()
res_iter = fib(test_n)
iter_time = time.time() - start_time
print(f"Iterative Result: {res_iter} | Time: {iter_time:.6f} seconds")

# Test Recursive (Naive method)
start_time = time.time()
res_rec = fib_recursive(test_n)
rec_time = time.time() - start_time
print(f"Recursive Result: {res_rec} | Time: {rec_time:.6f} seconds")
print(f"Iterative is faster by {rec_time - iter_time:.6f} seconds!")

# 5
print("\n 5")
mod_val = 10
seq_length = 20
mod_sequence = [fib(i) % mod_val for i in range(seq_length)]

print("Standard Seq:", [fib(i) for i in range(seq_length)])
print(f"Modulo {mod_val} Seq: ", mod_sequence)