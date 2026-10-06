# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 2
# Date: 5/10/2026
# Description: Convert total seconds into hours, minutes, and seconds using floor division (//) and modulus (%).

# 1
print("1. Ask the user to input the total seconds. ")
secs = int(input("Enter total seconds: "))

h = secs // 3600
rem = secs % 3600
m = rem // 60
s = rem % 60

# 2
print("2: Print the result in the format hh:mm:ss. ")
print(f"Time: {h:02d}:{m:02d}:{s:02d}")

# 3
print("3: Verify by converting back: total_check = h*3600 + m*60 + s. ")
total_check = h * 3600 + m * 60 + s
print(f"Verification: {total_check} == {secs} is {total_check == secs}")

# 4
print("4:Extend to milliseconds → hours–minutes–seconds–milliseconds. ")
total_ms = int(input("Enter total milliseconds: "))

ms = total_ms % 1000
remaining_secs = total_ms // 1000

h = remaining_secs // 3600
rem = remaining_secs % 3600
m = rem // 60
s = rem % 60

print(f"{h} hours - {m} minutes - {s} seconds - {ms} milliseconds")

# 5
print("5: Convert 100,000 seconds into days, hours, minutes, and seconds. ")
secs_to_peel = 100000
units = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]

print(f"For {secs_to_peel} s:")
rem = secs_to_peel

for name, factor in units:
    value = rem // factor
    rem = rem % factor  # Update remainder for the next iteration
    
    if value > 0: # Add 's' for plural simply to match grammar
        print(f"{value} {name}s", end=" ")