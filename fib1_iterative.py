# Iterative Fibonacci with Step Count

def fibonacci_iterative(n):
    step_count = 0  # Initialize step count
    a, b = 0, 1
    for i in range(n):
        step_count += 1  # Counting each loop iteration
        a, b = b, a + b  # Updating values of a and b
    return a, step_count

# Input from the user
n = int(input("Enter the value of n: "))
result, step_count = fibonacci_iterative(n)

print(f"Fibonacci({n}) = {result}")
print(f"Step Count (Iterative): {step_count}")
