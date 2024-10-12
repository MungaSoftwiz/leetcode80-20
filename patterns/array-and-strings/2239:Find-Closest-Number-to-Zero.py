#!/usr/bin/python3

# https://leetcode.com/problems/find-closest-number-to-zero/description/
# difficulty: easy

# Problem
# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.

# Approach
# Break problem in two sentences. It;s self explanatory

# Solution: O(n) for Tc and O(1) for Sc


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for k in nums:
            if abs(k) < abs(closest):
                closest = k
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        return closest
