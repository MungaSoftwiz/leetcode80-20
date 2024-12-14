#!/usr/bin/python3

# https://leetcode.com/problems/product-of-array-except-self/description/
# difficulty: medium
# tags: prefix-postfix multiplication

# Problem
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# Approach: 
# Initialize prefix and postfix multiplications(hold running prod from left and right)
# create an array to hold the prefix and postfix product
# Compute prefix and postfix products - Iterate array from left to fill l_arr. Simultaneously vice versa for right.
# Combine prefix products. Multiply corresponding elements of l_arr and r_arr.

# Solution: O(n) for TC and 0(n) for SC.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult, r_mult = 1, 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i - 1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        return [i * j for i, j in zip(l_arr, r_arr)]
