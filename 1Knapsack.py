def knapsack_dp(weights, values, capacity):
    n = len(values)
    # Create a 2D DP array with (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Include the item and check the maximum value
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Skip the item
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Taking input from the user
n = int(input("Enter the number of items: "))
weights = []
values = []

for i in range(n):
    value = int(input(f"Enter the value of item {i + 1}: "))
    weight = int(input(f"Enter the weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

capacity = int(input("Enter the capacity of the knapsack: "))

# Solve the 0-1 Knapsack problem
max_value = knapsack_dp(weights, values, capacity)
print(f"Maximum value that can be obtained: {max_value}")
