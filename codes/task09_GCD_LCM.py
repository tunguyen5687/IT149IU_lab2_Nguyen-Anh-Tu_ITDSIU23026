# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 9
# Date: 5/10/2026
# Description: Compute GCD using Euclid's algorithm with a while loop, print steps, and calculate LCM.

import math

def gcd_euclid(a: int, b: int) -> int:
    print(f"a={a} b={b}")
    while b != 0:
        rem = a % b
        print(f"{a} % {b} = {rem}")
        a, b = b, rem
    return a

a_val = 84
b_val = 36

gcd_val = gcd_euclid(a_val, b_val)

lcm_val = (a_val * b_val) // gcd_val

print(f"gcd={gcd_val} lcm={lcm_val}")

check_gcd = math.gcd(a_val, b_val)
print(f"Check with math.gcd: {check_gcd} == {gcd_val} is {check_gcd == gcd_val}")