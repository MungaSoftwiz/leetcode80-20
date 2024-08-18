#!/usr/bin/python3

# https://leetcode.com/problems/running-sum-of-1d-array/description/
# difficulty: easy
# tags: prefix sum, array

# Problem
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Approach
# Prefix sum or cumulative sum pattern. The idea is to create a prefix_array of the running total
# that gets updated step by step as you move through the list.

# Solution: 0(n) for both time & space complexity

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_array = [0] * length
        prefix_array[0] = nums[0]
        for num in range(1, length):
            prefix_array[num] = prefix_array[num - 1] + nums[num]
        return prefix_array
