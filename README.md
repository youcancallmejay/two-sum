# Two Sum Problem and Solution

This repository contains a Python solution for the Two Sum problem from LeetCode. The problem involves finding two numbers in an array that add up to a given target value. The solution is implemented in the `main` function.

## Problem Description

Given an array of integers `nums` and an integer `target`, you need to return the indices of the two numbers such that they add up to the `target`. You can assume that each input will have exactly one solution, and you may not use the same element twice. The solution can be returned in any order.

### Example

Input: `nums = [2, 11, 7, 15], target = 9`

Output: `[0, 2]`

Explanation: `nums[0] + nums[2] = 2 + 7 = 9`, so the answer is `[0, 2]`.

## Solution

In this repository, I've provided a Python solution for the Two Sum problem. The solution uses a dictionary (hash table) to efficiently find the two numbers that add up to the target. The time complexity of the solution is O(n), where n is the length of the `nums` array.

Here's how the solution works:

1. Initialize an empty dictionary called `num_indices` to store numbers and their indices.
2. Iterate through the `nums` array using a `for` loop.
3. For each number, calculate the complement (target - current number).
4. Check if the complement is in the `num_indices` dictionary. If it is, print the indices of the two numbers and return them.
5. If the complement is not in the dictionary, add the current number to the dictionary with its index.
6. If no valid solution is found, return an empty list.

You can find the Python code in the repository's `main` function.
