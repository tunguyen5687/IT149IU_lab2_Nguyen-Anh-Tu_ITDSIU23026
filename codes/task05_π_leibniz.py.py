# Student's Name: Nguyễn Anh Tú
# StudentID: ITDSIU23026
# Course: Fundamentals of Programming (FoP)
# Lab 2 – Task 5
# Date: 5/10/2026
# Description: Approximate Pi using the Leibniz alternating series and calculate absolute error against math.pi.

# 1
print("\n1")
import math

epsilon = float(input("Enter error threshold: "))

sgn = 1.0
acc = 0.0
k = 0

while abs(math.pi - 4 * acc) >= epsilon:
    acc += sgn / (2 * k + 1)
    sgn *= -1
    k += 1

approx_pi = 4 * acc
print(f"Reached threshold {epsilon} after {k} terms.")
print(f"Approximation: {approx_pi:.6f} | True Pi: {math.pi:.6f}")

# 2
print("\n 2")
import matplotlib.pyplot as plt

def pi_leibniz(k_terms: int) -> float:
    sgn = 1.0
    acc = 0.0
    for k in range(k_terms):
        acc += sgn / (2 * k + 1)
        sgn *= -1
    return 4 * acc

terms_list = [10, 100, 1000, 10000, 100000]
errors = []

for t in terms_list:
    approx = pi_leibniz(t)
    errors.append(abs(math.pi - approx))

plt.figure(figsize=(6, 4))
plt.plot(terms_list, errors, marker='o', color='blue')
plt.xscale('log') 
plt.yscale('log') 
plt.title('Leibniz Series Convergence')
plt.xlabel('Number of Terms (Log Scale)')
plt.ylabel('Absolute Error (Log Scale)')
plt.grid(True, which="both", ls="--")
plt.show()

# 3
print("\n 3")
def pi_nilakantha(k_terms: int) -> float:
    if k_terms <= 0: return 3.0
    acc = 3.0
    sgn = 1.0
    for k in range(1, k_terms):
        d = 2 * k
        acc += sgn * (4.0 / (d * (d + 1) * (d + 2)))
        sgn *= -1
    return acc

test_terms = 50
leibniz_pi = pi_leibniz(test_terms)
nilakantha_pi = pi_nilakantha(test_terms)

print(f"Leibniz Error:    {abs(math.pi - leibniz_pi):.10f}")
print(f"Nilakantha Error: {abs(math.pi - nilakantha_pi):.10f}")
print("Conclusion: Nilakantha converges significantly faster.")

# 4
print("\n 4")
n_bars = 15
terms = []
labels = []

sgn = 1.0
for k in range(n_bars):
    term_val = sgn / (2 * k + 1)
    terms.append(term_val)
    labels.append(f"{'+' if sgn>0 else '-'}{2*k+1}")
    sgn *= -1

plt.figure(figsize=(8, 4))
plt.bar(range(n_bars), terms, color=['green' if t > 0 else 'red' for t in terms])
plt.axhline(0, color='black', linewidth=1)
plt.xticks(range(n_bars), labels)
plt.title('Alternating Signs in Leibniz Series')
plt.xlabel('Denominator')
plt.ylabel('Fractional Value')
plt.show()