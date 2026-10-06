# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 10
# Date: 5/10/2026
# Description: Generate the Collatz sequence for a positive integer and find the starting value below 1000 with the longest sequence.

def collatz(n: int):
    sequence = [n]
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        steps += 1
    return sequence, steps

test_n = 6
seq, stp = collatz(test_n)
print(f"n = {test_n}:", *seq, f"({stp} steps)")

max_steps = 0
best_start = 0

for i in range(1, 1000):
    _, stp = collatz(i)
    if stp > max_steps:
        max_steps = stp
        best_start = i

print(f"Longest below 1000: n = {best_start} with {max_steps} steps")