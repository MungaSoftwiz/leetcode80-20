#!/usr/bin/python3

# https://leetcode.com/problems/range-sum-query-immutable/description/
# difficulty: easy
# tags: prefix sum, array

# Problem
# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right
# Basically calculating the sum of elements between left and right index of an array(difference).

# Approach
# Prefix sum pattern. The idea is to create a prefix_sum array filled with zeros. We add one(1) to the
# length because of the inclusive addition of right element.

# Solution: 0(1) TC in function(simple substraction), O(n) SC(additional element at the beginning).


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0] * (len(nums) + 1)

        for num in range(len(nums)):
            self.prefix_sums[num + 1] = self.prefix_sums[num] + nums[num]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
