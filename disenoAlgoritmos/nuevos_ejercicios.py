
# 1. Fibonacci Sequence (Recursion)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 2. Climbing Stairs (Dynamic Programming)
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 3. Min Cost Climbing Stairs (Dynamic Programming)
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]

# 4. House Robber (Dynamic Programming)
# You are a professional robber planning to rob houses along a street.
# Adjacent houses have security systems connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]

# 5. Coin Change (Dynamic Programming)
# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# 6. Unique Paths (Dynamic Programming)
# There is a robot on an m x n grid. The robot is initially located at the top-left corner.
# The robot tries to move to the bottom-right corner. The robot can only move either down or right.
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

# 7. Longest Increasing Subsequence (Dynamic Programming)
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 8. Maximum Subarray (Kadane's Algorithm)
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
def max_sub_array(nums):
    max_so_far = nums[0]
    current_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far

# 9. Rod Cutting (Dynamic Programming)
# Given a rod of length n and a list of prices of rods of length i, find the optimal way to cut the rod.
def rod_cutting(price, n):
    val = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = -float('inf')
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val
    return val[n]

# 10. Subset Sum (Dynamic Programming)
# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set
# with sum equal to given sum.
def is_subset_sum(set_nums, n, sum_val):
    subset = ([[False for i in range(sum_val + 1)]
            for i in range(n + 1)])
    for i in range(n + 1):
        subset[i][0] = True
    for i in range(1, sum_val + 1):
        subset[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum_val + 1):
            if j < set_nums[i-1]:
                subset[i][j] = subset[i-1][j]
            else:
                subset[i][j] = (subset[i-1][j] or
                                subset[i-1][j-set_nums[i-1]])
    return subset[n][sum_val]

if __name__ == "__main__":
    print("1. Fibonacci(10):", fibonacci(10))
    print("2. Climb Stairs(5):", climb_stairs(5))
    print("3. Min Cost Climbing Stairs([10, 15, 20]):", min_cost_climbing_stairs([10, 15, 20]))
    print("4. House Robber([1, 2, 3, 1]):", rob([1, 2, 3, 1]))
    print("5. Coin Change([1, 2, 5], 11):", coin_change([1, 2, 5], 11))
    print("6. Unique Paths(3, 7):", unique_paths(3, 7))
    print("7. LIS([10, 9, 2, 5, 3, 7, 101, 18]):", length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print("8. Max Subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]):", max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("9. Rod Cutting([1, 5, 8, 9, 10, 17, 17, 20], 8):", rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print("10. Subset Sum([3, 34, 4, 12, 5, 2], 9):", is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9))
