class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value of knapsack
    for item in items:
        if capacity >= item.weight:
            # If the knapsack can fit the entire item, take it all
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fractional part of the item that fits in the remaining capacity
            total_value += item.ratio * capacity
            break

    return total_value

# Taking input from the user
n = int(input("Enter the number of items: "))
items = []
for i in range(n):
    value = float(input(f"Enter the value of item {i + 1}: "))
    weight = float(input(f"Enter the weight of item {i + 1}: "))
    items.append(Item(value, weight))

capacity = float(input("Enter the capacity of the knapsack: "))

# Solve the fractional knapsack problem
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in knapsack: {max_value:.2f}")
