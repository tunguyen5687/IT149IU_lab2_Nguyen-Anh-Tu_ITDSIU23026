# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 7
# Date: 5/10/2026
# Description: Convert binary string to decimal integer using positional weights and iterative accumulation.

# 1
print("\n 1")
def bin_to_dec(bits: str) -> int:
    val = 0
    for ch in bits:
        val = val * 2 + (1 if ch == '1' else 0)
    return val
user_bits = input("Enter a binary string: ")
dec_val = bin_to_dec(user_bits)
print(f"Binary '{user_bits}' to Decimal: {dec_val}")

# 2
print("\n 2")
builtin_val = int(user_bits, 2)
print(f"Built-in int('{user_bits}', 2) result: {builtin_val}")
print(f"Match? {dec_val == builtin_val}")

# 3
print("\n 3")
def dec_to_bin(n: int) -> str:
    if n == 0:
        return "0"
    
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits 
        n = n // 2
    return bits

test_dec = 13
print(f"Decimal {test_dec} to Binary string: '{dec_to_bin(test_dec)}'")

# 4
print("\n 4")
while True:
    valid_bits = input("Enter a binary string: ")
    if valid_bits != "" and all(c in '01' for c in valid_bits):
        break
    print("Invalid input! Please enter only '0' or '1'.")

result = bin_to_dec(valid_bits)
print(f"Validated Binary '{valid_bits}' to Decimal: {result}")

# 5
print("\n 5")
import matplotlib.pyplot as plt

bits_str = '1101'
length = len(bits_str)

positions = list(range(length - 1, -1, -1))
powers = [2 ** p for p in positions]

colors = ['blue' if b == '1' else 'lightgray' for b in bits_str]

plt.figure(figsize=(6, 4))
plt.bar([str(p) for p in positions], powers, color=colors)
plt.title(f"Positional Weights for Binary '{bits_str}'")
plt.xlabel("Bit Position (Power of 2)")
plt.ylabel("Weight Value")
plt.grid(axis='y', linestyle='--')
plt.show()