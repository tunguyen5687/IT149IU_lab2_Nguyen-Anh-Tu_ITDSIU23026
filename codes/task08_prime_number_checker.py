# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 8
# Date: 5/10/2026
# Description: Check prime numbers up to square root of n and print all primes below 100 formatted in a grid.

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        # TODO: return False if i divides n
        if n % i == 0:
            return False
        i += 1
    return True

count = 0
for n in range(2, 100):
    if is_prime(n):
        # TODO: print n in width 4 without a newline; start a new line after 10 primes
        print(f"{n:>4}", end="")
        count += 1
        
        # Start a new line after exactly 10 primes
        if count % 10 == 0:
            print()

# Ensure the final count prints on a new line if the last row didn't perfectly hit 10 items
if count % 10 != 0:
    print()

print(count, "primes below 100")